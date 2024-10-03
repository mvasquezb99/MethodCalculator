import sympy as sp
from flask import jsonify
from sympy import *


def regla_falsa2(fx, a, b, tol, n_iter):
    E = []
    Xmi = []
    Fxmi = []
    c = 0
    xn = a
    x = sp.Symbol("x")
    fa = float(sp.N(sp.sympify(fx).subs(x, xn)))
    xn = b
    fb = float(sp.N(sp.sympify(fx).subs(x, xn)))
    if fa == 0:
        print(a, "Es rais de", fx)
        return
    elif fb == 0:
        print(a, "Es rais de", fx)
        return
    elif fa * fb < 0:
        xm = b - ((fb * (a - b)) / (fa - fb))
        Xmi.append(xm)
        xn = xm
        fxm = float(sp.N(sp.sympify(fx).subs(x, xn)))
        Fxmi.append(fxm)
        err_rel = float(100)
        E.append(err_rel)
        while E[c] > tol and fxm != 0 and c < n_iter:
            if fxm < 0:
                a = xm
                xn = a
                fa = float(sp.N(sp.sympify(fx).subs(x, xn)))
            else:
                b = xm
                xn = b
                fb = float(sp.N(sp.sympify(fx).subs(x, xn)))
            xm_temp = xm
            xm = b - ((fb * (a - b)) / (fa - fb))
            Xmi.append(xm)
            xn = xm
            fxm = float(sp.N(sp.sympify(fx).subs(x, xn)))
            Fxmi.append(fxm)

            if xm != 0:
                err_rel = abs((xm - xm_temp) / xm)
            else:
                err_rel = abs(xm - xm_temp)  # No debería pasar

            E.append(float(err_rel))
            c += 1
        if fxm == 0:
            msg = (
                "\nRESULTADO:\n\n\t fxm: "
                + str(fxm)
                + " x: "
                + str(xm)
                + " ε: "
                + str(err_rel)
                + "\n"
            )
            return jsonify(
                {
                    "msg": msg,
                    "status": 200,
                    "Xm": Xmi,
                    "fxm": Fxmi,
                    "ε": E,
                }
            )
        elif err_rel < tol:

            msg = (
                "\nRESULTADO APROXIMADO:\n\n\t fxm: "
                + str(fxm)
                + " x: "
                + str(xm)
                + " ε: "
                + str(err_rel)
                + "\n"
            )

            return jsonify(
                {
                    "msg": msg,
                    "status": 200,
                    "Xm": Xmi,
                    "fxm": Fxmi,
                    "ε": E,
                }
            )
        else:
            msg = "Fracaso en " + str(n_iter) + " iteraciones"
            return jsonify(
                {
                    "Xm": Xmi,
                    "fxm": Fxmi,
                    "ε": E,
                    "message": msg,
                    "status": 400,
                }
            )
    else:
        msg = "Intervalo entre [" + str(a) + "," + str(b) + "] es inadecuado"
        return jsonify(
            {
                "message": msg,
                "status": 400,
            }
        )

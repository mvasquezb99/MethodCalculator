import sympy as sp
from flask import jsonify
from sympy import *


def bisec(fx, a, b, tol, n_iter):
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
        xm = (a + b) / 2
        Xmi.append(xm)
        xn = xm
        fxm = float(sp.N(sp.sympify(fx).subs(x, xn)))
        Fxmi.append(fxm)
        err = float(100)
        E.append(err)
        while E[c] > tol and fxm != 0 and c < n_iter:
            if fxm < 0:
                a = xm
                xn = a
                fa = float(sp.N(sp.sympify(fx).subs(x, xn)))
            else:
                b = xm
                xn = b
                fb = float(sp.N(sp.sympify(fx).subs(x, xn)))
            x_temp = xm
            xm = (a + b) / 2
            Xmi.append(xm)
            xn = xm
            fxm = float(sp.N(sp.sympify(fx).subs(x, xn)))
            Fxmi.append(fxm)
            err = abs(xm - x_temp)
            E.append(float(err))
            c += 1
        if fxm == 0:
            msg = "RESULTADO: fxm: " + str(fxm) + " x: " + str(xm) + " E: " + str(err)
            return jsonify(
                {
                    "msg": msg,
                    "status": 200,
                    "Xm": Xmi,
                    "fxm": Fxmi,
                    "E": E,
                }
            )
        elif err < tol:
            msg = "RESULTADO: fxm: " + str(fxm) + " x: " + str(xm) + " E: " + str(err)
            return jsonify(
                {
                    "msg": msg,
                    "status": 200,
                    "Xm": Xmi,
                    "fxm": Fxmi,
                    "E": E,
                }
            )
        else:
            msg = "Fracaso en " + str(n_iter) + " iteraciones"
            return jsonify(
                {
                    "Xm": Xmi,
                    "fxm": Fxmi,
                    "E": E,
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

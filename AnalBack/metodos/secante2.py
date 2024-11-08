import sympy as sp
from flask import jsonify
from sympy import *


def seca2(fx, x0, x1, tol, n_iter):
    E = []
    Er = []
    Xn = []
    Fn = []
    xn = x0
    x = sp.Symbol("x")
    f0 = float(sp.N(sp.sympify(fx).subs(x, xn)))
    c = 0
    err = float(100)
    Fn.append(f0)
    E.append(err)
    Er.append(err)
    Xn.append(xn)
    xn = x1
    f1 = float(sp.N(sp.sympify(fx).subs(x, xn)))
    Fn.append(f1)
    err = abs(x0 - x1)
    errR = abs(err / x1)
    E.append(err)
    Er.append(errR)
    Xn.append(xn)
    while errR > tol and f0 != 0 and f1 != 0 and c < n_iter:
        xn = xn - ((f1 * (x1 - x0)) / (f1 - f0))
        x0 = x1
        x1 = xn
        f0 = f1
        f1 = float(sp.N(sp.sympify(fx).subs(x, xn)))
        if f1 == sp.nan or f1 == oo or f1 == -oo:
            f1 = sys.float_info.max
            break
        Fn.append(f1)
        Xn.append(xn)
        c += 1
        err = abs(Xn[c + 1] - Xn[c])
        errR = abs(err / xn)
        E.append(err)
        Er.append(errR)
    if f1 == 0:
        msg = "\nRESULTADO:\n\n\t fe:", f1, "x: ", xn, "Er: ", errR, "\n"
        return jsonify(
            {
                "msg": msg,
                "status": 200,
                "Xm": Xn,
                "fxm": Fn,
                "E": Er,
            }
        )
    elif err < tol:
        msg = "\nRESULTADO APROXIMADO:\n\n\t fe:", f1, "x: ", xn, "Er: ", errR, "\n"
        return jsonify(
            {
                "msg": msg,
                "status": 200,
                "Xm": Xn,
                "fxm": Fn,
                "E": Er,
            }
        )
    else:
        msg = "Fracaso en " + str(n_iter) + " iteraciones"
        return jsonify(
            {
                "Xm": Xn,
                "fxm": Fn,
                "E": Er,
                "message": msg,
                "status": 400,
            }
        )

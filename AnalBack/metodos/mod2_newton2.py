import sympy as sp
from flask import jsonify
from sympy import *


def mnt(fx, x0, tol, n_iter):
    E = []
    Er = []
    Xn = []
    Fn = []
    xn = x0
    x = sp.Symbol("x")
    fe = float(sp.N(sp.sympify(fx).subs(x, xn)))
    g1 = sp.diff(fx, x)
    df1 = float(sp.N(g1.subs(x, x0)))
    g2 = sp.diff(g1, x)
    df2 = float(sp.N(g2.subs(x, x0)))
    c = 0
    err = float(100)
    errR = float(100)
    Fn.append(fe)
    E.append(err)
    Er.append(errR)
    Xn.append(xn)
    while errR > tol and fe != 0 and c < n_iter:
        xn = xn - (fe * df1) / (df1**2 - (fe * df2))
        df1 = float(sp.N(g1.subs(x, xn)))
        df2 = float(sp.N(g2.subs(x, xn)))
        fe = float(sp.N(sp.sympify(fx).subs(x, xn)))
        Fn.append(fe)
        Xn.append(xn)
        c += 1
        err = abs(Xn[c] - Xn[c - 1])
        errR = abs(err / xn)
        E.append(err)
        Er.append(errR)
    if fe == 0:
        msg = "\nRESULTADO:\n\n\t fe:", fe, "x: ", xn, "Er: ", errR, "\n"
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
        msg = "\nRESULTADO APROXIMADO:\n\n\t fe:", fe, "x: ", xn, "Er: ", errR, "\n"
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

import sys

import sympy as sp
from flask import jsonify
from sympy import *


def mnt(fx, m, x0, tol, n_iter):
    E = []
    Xn = []
    Fn = []
    xn = x0
    x = sp.Symbol("x")
    fe = float(sp.N(sp.sympify(fx).subs(x, xn)))
    g = sp.diff(fx, x)
    df = float(sp.N(g.subs(x, x0)))
    c = 0
    err = float(100)
    Fn.append(fe)
    E.append(err)
    Xn.append(xn)
    while err > tol and fe != 0 and c < n_iter:
        xn = xn - (m * (fe / df))
        df = float(sp.N(g.subs(x, xn)))
        if df == sp.nan or df == oo or df == -oo:
            df = sys.float_info.max
            break
        fe = float(sp.N(sp.sympify(fx).subs(x, xn)))
        if fe == sp.nan or fe == oo or fe == -oo:
            fe = sys.float_info.max
            break
        Fn.append(fe)
        Xn.append(xn)
        c += 1
        err = abs(Xn[c] - Xn[c - 1])
        E.append(err)
    if fe == 0:
        msg = "\nRESULTADO:\n\n\t fe:", fe, "x: ", xn, "E: ", err, "\n"
        return jsonify(
            {
                "msg": msg,
                "status": 200,
                "Xm": Xn,
                "fxm": Fn,
                "E": E,
            }
        )
    elif err < tol:
        msg = "\nRESULTADO APROXIMADO:\n\n\t fe:", fe, "x: ", xn, "E: ", err, "\n"
        return jsonify(
            {
                "msg": msg,
                "status": 200,
                "Xm": Xn,
                "fxm": Fn,
                "E": E,
            }
        )
    else:
        msg = "Fracaso en " + str(n_iter) + " iteraciones"
        return jsonify(
            {
                "Xm": Xn,
                "fxm": Fn,
                "E": E,
                "message": msg,
                "status": 400,
            }
        )

import sympy as sp
from flask import jsonify
from sympy import *


def nt2(fx, x0, tol, n_iter):
    E = []
    Xn = []
    Fn = []
    xn = x0
    x = sp.Symbol("x")
    fe = float(sp.N(sp.sympify(fx).subs(x, xn)))
    g = sp.diff(fx, x)
    df = float(sp.N(g.subs(x, xn)))
    c = 0
    # tolerancia = 5 * 10 ** (-tol)
    err_rel = float(100)
    Fn.append(fe)
    E.append(err_rel)
    Xn.append(xn)
    while err_rel > tol and fe != 0 and c < n_iter:
        xn_new = xn - (fe / df)
        df = float(sp.N(g.subs(x, xn_new)))
        if df == sp.nan or df == oo or df == -oo:
            df = sys.float_info.max
            break
        fe = float(sp.N(sp.sympify(fx).subs(x, xn_new)))
        if fe == sp.nan or fe == oo or fe == -oo:
            fe = sys.float_info.max
            break
        Fn.append(fe)
        Xn.append(xn_new)
        c += 1

        if xn_new != 0:
            err_rel = abs(xn_new - xn) / abs(xn_new)
        else:
            err_rel = abs(xn_new - xn)  # No deberia pasar

        E.append(err_rel)

        xn = xn_new

    if fe == 0:
        msg = "\nRESULTADO:\n\n\t fe:", fe, "x: ", xn, "Er: ", err_rel, "\n"
        return jsonify(
            {
                "msg": msg,
                "status": 200,
                "Xm": Xn,
                "fxm": Fn,
                "E": E,
            }
        )
    elif err_rel < tol:
        msg = "\nRESULTADO APROXIMADO:\n\n\t fe:", fe, "x: ", xn, "Er: ", err_rel, "\n"
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

import sympy as sp
from flask import jsonify
from sympy import *


def seca(fx, x0, x1, tol, n_iter):
    E = []
    Xn = []
    Fn = []
    xn = x0
    x = sp.Symbol("x")
    f0 = float(sp.N(sp.sympify(fx).subs(x, xn)))
    c = 0
    err = float(100)
    Fn.append(f0)
    E.append(err)
    Xn.append(xn)
    xn = x1
    f1 = float(sp.N(sp.sympify(fx).subs(x, xn)))
    Fn.append(f1)
    err = abs(x0 - x1)
    E.append(err)
    Xn.append(xn)
    while err > tol and f0 != 0 and f1 != 0 and c < n_iter:
        xn = xn - ((f1 * (x1 - x0)) / (f1 - f0))
        x0 = x1
        x1 = xn
        f0 = f1
        f1 = float(sp.N(sp.sympify(fx).subs(x, xn)))
        Fn.append(f1)
        Xn.append(xn)
        c += 1
        err = abs(Xn[c + 1] - Xn[c])
        E.append(err)
    if f1 == 0:
        msg = "\nRESULTADO:\n\n\t fe:", f1, "x: ", xn, "E: ", err, "\n"
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
        msg = "\nRESULTADO APROXIMADO:\n\n\t fe:", f1, "x: ", xn, "E: ", err, "\n"
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


def main():
    fx = input("fx: ")
    x0 = float(input("x0: "))
    x1 = float(input("x1: "))
    tol = float(input("tol: "))
    n_iter = float(input("n_iter: "))
    seca(fx, x0, x1, tol, n_iter)


if __name__ == "__main__":
    main()

import math

import numpy as np
import pandas as pd


def nt(fx, g, x0, tol, n_iter):
    E = []
    Xn = []
    Fn = []
    x = x0
    fe = eval(fx)
    df = eval(g)
    c = 0
    err = float(100)
    Fn.append(fe)
    E.append(err)
    Xn.append(x)
    while err > tol and fe != 0 and c < n_iter:
        x = x - fe / df
        df = eval(g)
        fe = eval(fx)
        Fn.append(fe)
        Xn.append(x)
        c += 1
        err = abs(Xn[c] - Xn[c - 1])
        E.append(err)
    if fe == 0:
        print("\nRESULTADO:\n\n\t fe:", fe, "x: ", x, "E: ", err, "\n")
        tabla = [Xn, Fn, E]
        tabla = np.transpose(tabla)
        tabla = pd.DataFrame(tabla, columns=["x", "fn", "E"])  # type: ignore
        tabla.index = np.arange(1, len(tabla) + 1)
        print(tabla)
    elif err < tol:
        print("\nRESULTADO:\n\n\t fe:", fe, "x: ", x, "E: ", err, "\n")
        tabla = [Xn, Fn, E]
        tabla = np.transpose(tabla)
        tabla = pd.DataFrame(tabla, columns=["x", "fn", "E"])  # type: ignore
        tabla.index = np.arange(1, len(tabla) + 1)
        print(tabla)
    else:
        print("Fracaso en", n_iter, "iteraciones")

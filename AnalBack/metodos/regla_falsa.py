import math

import numpy as np
import pandas as pd


def bisec(fx, a, b, tol, n_iter):
    E = []
    Xmi = []
    Fxmi = []
    c = 0
    x = a
    fa = eval(fx)
    x = b
    fb = eval(fx)
    if fa == 0:
        print(a, "Es rais de", fx)
        return
    elif fb == 0:
        print(a, "Es rais de", fx)
        return
    elif fa * fb < 0:
        xm = b - ((fb * (a - b)) / (fa - fb))
        Xmi.append(xm)
        x = xm
        fxm = eval(fx)
        Fxmi.append(fxm)
        err = float(100)
        E.append(err)
        while E[c] > tol and fxm != 0 and c < n_iter:
            if fxm < 0:
                a = xm
                x = a
                fa = eval(fx)
            else:
                b = xm
                x = b
                fb = eval(fx)
            x_temp = xm
            xm = b - ((fb * (a - b)) / (fa - fb))
            Xmi.append(xm)
            x = xm
            fxm = eval(fx)
            Fxmi.append(fxm)
            err = abs(xm - x_temp)
            E.append(float(err))
            c += 1
        if fxm == 0:
            # print(xm, "es la faiz de", fx)
            print("\nRESULTADO:\n\n\t fxm:", fxm, "x: ", xm, "E: ", err, "\n")
            tabla = [Xmi, Fxmi, E]
            tabla = np.transpose(tabla)
            tabla = pd.DataFrame(tabla, columns=["xm", "f(xm)", "E"])  # type: ignore
            tabla.index = np.arange(1, len(tabla) + 1)
            print(tabla)
        elif err < tol:
            print("\nRESULTADO:\n\n\t fxm:", fxm, "x: ", xm, "E: ", err, "\n")
            tabla = [Xmi, Fxmi, E]
            tabla = np.transpose(tabla)
            tabla = pd.DataFrame(tabla, columns=["xm", "f(xm)", "E"])  # type: ignore
            tabla.index = np.arange(1, len(tabla) + 1)
            print(tabla)
        else:
            print("Fracaso en", n_iter, "iteraciones")
    else:
        print("Intervalo entre [" + str(a) + "," + str(b) + "] es inadecuado")

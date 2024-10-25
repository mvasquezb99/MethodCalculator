import numpy as np
import pandas as pd
from flask import jsonify


def newton_interpolation(x_str, y_str):

    x = np.array([float(num) for num in x_str.split()])
    y = np.array([float(num) for num in y_str.split()])

    n = len(x)
    tabla = pd.DataFrame(np.zeros((n, n + 1)))

    tabla.iloc[:, 0] = x
    tabla.iloc[:, 1] = y

    for j in range(2, n + 1):
        for i in range(j - 1, n):
            tabla.iloc[i, j] = (tabla.iloc[i, j - 1] - tabla.iloc[i - 1, j - 1]) / (
                tabla.iloc[i, 0] - tabla.iloc[i - j + 1, 0]
            )

    # print("\n Tabla de diferencias divididas: \n", tabla)

    coef = np.diag(tabla, +1)
    coef = np.concatenate(([x[0]], coef))
    pol = np.array([coef[0]])
    acum = np.array([1])  # This corresponds to the accumulated product term

    for i in range(n - 1):
        pol = np.concatenate(([0], pol))
        acum = np.convolve(acum, [1, -x[i]])
        pol = pol + x[i + 1] * acum  # Before: pol = pol + coef[i + 1] * acum

    pol_str = ""
    for i in range(n):
        if i == n - 1:
            pol_str += f"{pol[i]:.4f}"
        else:
            pol_str += f"{pol[i]:.4f}x^{n - i} + "

    # print("\nPolinomio de Newton: ", pol_str)

    return jsonify(
        {
            "pol": pol_str,
            "status": 200,
        }
    )

import numpy as np
from flask import jsonify


def lagrange_interpolation(x_str, y_str):

    x = np.array([float(num) for num in x_str.split()])
    y = np.array([float(num) for num in y_str.split()])

    n = len(x)
    Tabla = np.zeros((n, n))  # Initialize the table to store intermediate results

    for i in range(n):
        Li = np.array([1])  # Initialize Li as 1
        den = 1  # Denominator term

        for j in range(n):
            if j != i:
                paux = np.array([1, -x[j]])
                # Convolve the current Li with (x - x_j)
                Li = np.convolve(Li, paux)
                den *= x[i] - x[j]

        Tabla[i, :] = y[i] * Li / den

    # Sum the rows of the table to get the final polynomial
    pol = np.sum(Tabla, axis=0)

    pol_str = ""
    for i in range(n):
        if i == n - 1:
            pol_str += f"{pol[i]:.4f}"
        else:
            pol_str += f"{pol[i]:.4f}x^{n - i} + "

    x_vals = np.linspace(min(x), max(x), 500)
    y_vals = np.polyval(pol, x_vals)

    return jsonify(
        {
            "pol": pol_str,
            "x_vals": x_vals.tolist(),
            "y_vals": y_vals.tolist(),
            "status": 200,
        }
    )

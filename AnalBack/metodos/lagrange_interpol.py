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
                # Polynomial factor (x - x_j) in Li
                paux = np.array([1, -x[j]])
                # Convolve the current Li with (x - x_j)
                Li = np.convolve(Li, paux)
                # Update the denominator
                den *= x[i] - x[j]

        # Store the term y_i * L_i / denominator in the table
        Tabla[i, :] = y[i] * Li / den

    # Sum the rows of the table to get the final polynomial
    pol = np.sum(Tabla, axis=0)

    pol_str = ""
    for i in range(n):
        if i == n - 1:
            pol_str += f"{pol[i]:.4f}"
        else:
            pol_str += f"{pol[i]:.4f}x^{n - i} + "

    return jsonify(
        {
            "pol": pol_str,
            "status": 200,
        }
    )

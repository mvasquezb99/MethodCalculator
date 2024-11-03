import numpy as np
from flask import jsonify


def vandermonde(x, y):
    x = np.array([float(num) for num in x.split()])
    y = np.array([float(num) for num in y.split()])

    x = np.transpose(x)
    y = np.transpose(y)

    # V = np.column_stack([x**3, x**2, x, np.ones(len(x))])
    V = np.vander(x, increasing=False)  # Vandermonde matrix in decreasing powers

    b = y

    pol = np.linalg.solve(V, b)

    n = len(pol)
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

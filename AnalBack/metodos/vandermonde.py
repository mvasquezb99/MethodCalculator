import numpy as np
from flask import jsonify


def vandermonde(x, y):
    x = np.array([float(num) for num in x.split()])
    y = np.array([float(num) for num in y.split()])

    x = np.transpose(x)
    y = np.transpose(y)

    V = np.column_stack([x**3, x**2, x, np.ones(len(x))])

    b = y

    pol = np.linalg.solve(V, b)

    n = len(pol)
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

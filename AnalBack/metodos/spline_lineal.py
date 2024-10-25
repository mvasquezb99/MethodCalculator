import numpy as np
from flask import jsonify


def spline_lineal(x_str, y_str):
    d = 1
    polinomios = []
    x = np.array([float(num) for num in x_str.split()])
    y = np.array([float(num) for num in y_str.split()])

    n = len(x)
    A = np.zeros(((d + 1) * (n - 1), (d + 1) * (n - 1)))  # Initialize matrix A
    b = np.zeros(((d + 1) * (n - 1), 1))  # Initialize vector b

    c = 0  # Indexing in Python starts from 0
    h = 0

    # First loop: fill A and b for i = 1 to n-1
    for i in range(n - 1):
        A[i, c] = x[i]
        A[i, c + 1] = 1
        b[i] = y[i]
        c += 2
        h += 1

    # Second loop: fill A and b for i = 2 to n
    c = 0  # Reset c
    for i in range(1, n):  # In Python, range(1, n) starts from 1 and goes up to n-1
        A[h, c] = x[i]
        A[h, c + 1] = 1
        b[h] = y[i]
        c += 2
        h += 1

        # Solve the system A * val = b
    val = np.linalg.solve(A, b)  # Solving instead of computing inverse

    # Reshape 'val' to a (n-1) x (d+1) matrix and transpose it
    Tabla = val.reshape(n - 1, d + 1).T

    # Compute the polynomial values for each interval
    for i in range(n - 1):
        # Extract coefficients for the i-th interval
        a_i = Tabla[0, i]  # Slope of the line
        b_i = Tabla[1, i]  # Intercept

        # Print the polynomial function for the interval
        if i == n - 2:  # Last segment
            polinomios.append(
                f"f(x) = {a_i:.2f} * x + {b_i:.2f} for {x[i]} <= x <= {x[i + 1]}"
            )
        else:
            polinomios.append(
                f"f(x) = {a_i:.2f} * x + {b_i:.2f} for {x[i]} <= x < {x[i + 1]}"
            )

    return jsonify(
        {
            "pol_arr": polinomios,
            "status": 200,
        }
    )

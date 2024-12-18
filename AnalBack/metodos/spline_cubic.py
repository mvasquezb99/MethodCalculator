import numpy as np
from flask import jsonify
from sympy import pprint


def spline_cubic(x_str, y_str):
    polinomios = []
    polinomios_range = []
    d = 3
    x = np.array([float(num) for num in x_str.split()])
    y = np.array([float(num) for num in y_str.split()])

    dict_xy = {}
    for i in range(len(x)):
        dict_xy[x[i]] = y[i]

    dict_xy = dict(sorted(dict_xy.items()))
    pprint(dict_xy)

    x = np.array(list(dict_xy.keys()))
    y = np.array(list(dict_xy.values()))

    cua = x**2
    cub = x**3  # Cube of x elements

    n = len(x)
    A = np.zeros(((d + 1) * (n - 1), (d + 1) * (n - 1)))  # Initialize matrix A
    b = np.zeros(((d + 1) * (n - 1), 1))  # Initialize vector b

    c = 0
    h = 0

    # First loop: fill A and b for i = 1 to n-1
    for i in range(n - 1):
        A[i, c] = cub[i]  # cub(i) in MATLAB corresponds to cub[i] in Python
        A[i, c + 1] = cua[i]  # cua(i) in MATLAB corresponds to cua[i] in Python
        A[i, c + 2] = x[i]  # x(i) in MATLAB corresponds to x[i] in Python
        A[i, c + 3] = 1  # Constant term
        b[i] = y[i]  # b(i) in MATLAB corresponds to b[h] in Python
        c += 4
        h += 1

    # Second loop: fill A and b for i = 2 to n
    c = 0  # Reset c
    for i in range(1, n):  # range(1, n) in Python corresponds to i = 2 to n in MATLAB
        A[h, c] = cub[i]  # cub(i) in MATLAB corresponds to cub[i] in Python
        A[h, c + 1] = cua[i]  # cua(i) in MATLAB corresponds to cua[i] in Python
        A[h, c + 2] = x[i]  # x(i) in MATLAB corresponds to x[i] in Python
        A[h, c + 3] = 1  # Constant term
        b[h] = y[i]  # b(i) in MATLAB corresponds to b[h] in Python
        c += 4
        h += 1

    # Third loop: fill A and b for i = 2 to n-1
    c = 0  # Reset c
    for i in range(
        1, n - 1
    ):  # range(2, n) in MATLAB corresponds to range(1, n-1) in Python
        A[h, c] = 3 * cua[i]  # 3*cua(i)
        A[h, c + 1] = 2 * x[i]  # 2*x(i)
        A[h, c + 2] = 1  # Constant term
        A[h, c + 4] = -3 * cua[i]  # -3*cua(i)
        A[h, c + 5] = -2 * x[i]  # -2*x(i)
        A[h, c + 6] = -1  # Constant term
        b[h] = 0  # b(h) = 0
        c += 4
        h += 1

    # Fourth loop: fill A and b for i = 2 to n-1
    c = 0  # Reset c
    for i in range(
        1, n - 1
    ):  # range(2, n-1) in MATLAB corresponds to range(1, n-1) in Python
        A[h, c] = 6 * x[i]  # 6*x(i)
        A[h, c + 1] = 2  # Constant term
        A[h, c + 4] = -6 * x[i]  # -6*x(i)
        A[h, c + 5] = -2  # Constant term
        b[h] = 0  # b(h) = 0
        c += 4
        h += 1

    # Last two conditions for the boundary
    A[h, 0] = 6 * x[0]  # 6*x(1)
    A[h, 1] = 2  # Constant term
    b[h] = 0  # b(h) = 0
    h += 1

    A[h, c] = 6 * x[-1]  # 6*x(end)
    A[h, c + 1] = 2  # Constant term
    b[h] = 0  # b(h) = 0

    val = np.linalg.solve(A, b)

    # Reshape 'val' to a (n-1) x (d+1) matrix and transpose it
    Tabla = val.reshape(n - 1, -1).T  # Automatically gets the right shape

    print("Polinomios cúbicos:")

    # Compute the polynomial values for each interval
    for i in range(n - 1):
        # Extract coefficients for the i-th interval
        a_i = Tabla[0, i]  # Cubic coefficient
        b_i = Tabla[1, i]  # Quadratic coefficient
        c_i = Tabla[2, i]  # Linear coefficient
        d_i = Tabla[3, i]  # Constant coefficient

        # Print the polynomial function for the interval
        polinomios.append(f"{a_i} * x^3 + {b_i} * x^2 + {c_i} * x + {d_i}")
        polinomios_range.append(f"{x[i]} <= x < {x[i + 1]}")

    print(polinomios)
    print(polinomios_range)

    return jsonify(
        {
            "pol": polinomios,
            "pol_range": polinomios_range,
            "status": 200,
        }
    )

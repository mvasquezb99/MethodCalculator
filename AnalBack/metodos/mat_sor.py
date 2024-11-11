import re

import numpy as np
from flask import jsonify


# Funcion para parsear matrices
def parse_matrix(A_str):
    return np.array(
        [list(map(float, re.findall(r"-?\d+\.?\d*", row))) for row in A_str.split(";")]
    )


def mat_sor(A, b, x0, tol, n_iter, w):

    A = parse_matrix(A)
    b = parse_matrix(b)
    x0 = parse_matrix(x0)

    S = []
    E = []
    c = 0
    xn = -1
    err = float(100)
    E.append(err)
    S.append(x0.tolist())
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    T = np.dot(np.linalg.inv(D - w * L), ((1 - w) * D + w * U))
    C = w * np.dot(np.linalg.inv(D - w * L), b)
    while err > tol and c < n_iter:
        xn = np.dot(T, x0) + C
        err = np.linalg.norm(xn - x0, np.inf)
        x0 = xn
        c += 1
        S.append(np.round(np.linalg.matrix_transpose(xn), 4).tolist())
        # S.append(np.linalg.matrix_transpose(xn).tolist())
        E.append(err)
    if err < tol:
        msg = "\nRESULTADO:\n\n\t", "S: ", S[-1], "E: ", E[-1], "\n"
        radio_espectral = np.max(np.abs(np.linalg.eigvals(T)))
        return jsonify(
            {
                "msg": msg,
                "status": 200,
                "S": S,
                "E": E,
                "RE": radio_espectral,
            }
        )
    else:
        msg = "la solucion no converge con numero de iteraciones: " + str(c)
        radio_espectral = np.max(np.abs(np.linalg.eigvals(T)))
        return jsonify(
            {
                "msg": msg,
                "status": 400,
                "S": S,
                "E": E,
                "RE": radio_espectral,
            }
        )

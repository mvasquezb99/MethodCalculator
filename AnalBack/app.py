from flask import Flask, jsonify, request
from flask_cors import CORS
from metodos import (
    biseccion,
    biseccion2,
    mat_jacobi,
    mat_jacobi2,
    mat_scidel,
    mat_scidel2,
    mod1_newton,
    mod2_newton,
    newton,
    newton2,
    punto_fijo,
    punto_fijo2,
    regla_falsa,
    regla_falsa2,
    secante,
)

app = Flask(__name__)
cors = CORS(app, origins="*")


@app.route("/")
def home():
    return "<p>Home</p>"


@app.route("/biseccion", methods=["GET", "POST"])  # type: ignore
def biseccion_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "a": "",
                "b": "",
                "use_cs": "",  # if 1 then use relative error
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        a = float(request.get_json()["input"]["a"])
        b = float(request.get_json()["input"]["b"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            result = biseccion.bisec(fx, a, b, tol, n_iter)
        else:
            result = biseccion2.bisec2(fx, a, b, tol, n_iter)
        return result


@app.route("/reglaFalsa", methods=["GET", "POST"])  # type: ignore
def regla_falsa_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "a": "",
                "b": "",
                "use_cs": "",  # if 1 then use relative error
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        a = float(request.get_json()["input"]["a"])
        b = float(request.get_json()["input"]["b"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return regla_falsa.regla_falsa(fx, a, b, tol, n_iter)
        else:
            return regla_falsa2.regla_falsa2(fx, a, b, tol, n_iter)
        # TODO: Check thath the method is correct


@app.route("/puntoFijo", methods=["GET", "POST"])
def punto_fijo_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "g": "",
                "x0": "",
                "use_cs": "",  # if 1 then use relative error
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        g = request.get_json()["input"]["g"]
        x0 = float(request.get_json()["input"]["x0"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return punto_fijo2.pf2(fx, g, x0, tol, n_iter)
        else:
            return punto_fijo.pf(fx, g, x0, tol, n_iter)


@app.route("/newton", methods=["GET", "POST"])
def newton_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "x0": "",
                "use_cs": "",  # if 1 then use relative error
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        x0 = float(request.get_json()["input"]["x0"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return newton2.nt2(fx, x0, tol, n_iter)
        else:
            return newton.nt(fx, x0, tol, n_iter)


@app.route("/secante", methods=["GET", "POST"])
def secante_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "x0": "",
                "x1": "",
                "use_cs": "",  # if 1 then use relative error
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        x0 = float(request.get_json()["input"]["x0"])
        x1 = float(request.get_json()["input"]["x1"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return secante.seca(
                fx, x0, x1, tol, n_iter
            )  # TODO: cambiar por secante con error relativo
        return secante.seca(fx, x0, x1, tol, n_iter)


@app.route("/newton_mod1", methods=["GET", "POST"])
def newton_mod1_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "x0": "",
                "m": "",
                "use_cs": "",  # if 1 then use relative error
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["fx"]
        x0 = float(request.get_json()["input"]["x0"])
        m = float(request.get_json()["input"]["m"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return mod1_newton.mnt(fx, m, x0, tol, n_iter)
        else:
            return mod1_newton.mnt(fx, m, x0, tol, n_iter)


@app.route("/newton_mod2", methods=["GET", "POST"])
def newton_mod2_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "x0": "",
                "tol": "",
                "use_cs": "",  # if 1 then use relative error
                "n_iter": "",
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        x0 = float(request.get_json()["input"]["x0"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return mod2_newton.mnt(fx, x0, tol, n_iter)
        else:
            return mod2_newton.mnt(fx, x0, tol, n_iter)


@app.route("/mat_jacobi", methods=["GET", "POST"])
def mat_jacobi_route():
    if request.method == "GET":
        return jsonify(
            {
                "A": "",
                "b": "",
                "x0": "",
                "use_cs": "",  # if 1 then use relative error
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        A = request.get_json()["input"]["A"]
        b = request.get_json()["input"]["b"]
        x0 = request.get_json()["input"]["x0"]
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return mat_jacobi2.mat_jacobi2(A, b, x0, tol, n_iter)
        else:
            return mat_jacobi.mat_jacobi(A, b, x0, tol, n_iter)


@app.route("/mat_scidel", methods=["GET", "POST"])
def mat_scidel_route():
    if request.method == "GET":
        return jsonify(
            {
                "A": "",
                "b": "",
                "x0": "",
                "use_cs": "",  # if 1 then use relative error
                "tol": "",
                "n_iter": "",
            }
        )
    else:
        A = request.get_json()["input"]["A"]
        b = request.get_json()["input"]["b"]
        x0 = request.get_json()["input"]["x0"]
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return mat_scidel2.mat_scidel2(A, b, x0, tol, n_iter)
        else:
            return mat_scidel.mat_scidel(A, b, x0, tol, n_iter)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

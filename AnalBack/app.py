from flask import Flask, jsonify, request
from flask_cors import CORS
from metodos import (
    biseccion,
    mod1_mewton,
    mod2_newton,
    newton,
    punto_fijo,
    regla_falsa,
    secante,
)

# TODO: Add C.S to all the methods

app = Flask(__name__)
cors = CORS(app, origins="*")


@app.route("/")
def home():
    return "<p>Home</p>"


@app.route("/biseccion", methods=["GET", "POST"])  # type: ignore
def biseccion_route():
    if request.method == "GET":
        return "<p>Biseccion</p>"
    else:
        fx = request.get_json()["fx"]
        a = float(request.get_json()["a"])
        b = float(request.get_json()["b"])
        tol = float(request.get_json()["tol"])
        n_iter = float(request.get_json()["n_iter"])
        return biseccion.bisec(fx, a, b, tol, n_iter)


@app.route("/reglaFalsa", methods=["GET", "POST"])  # type: ignore
def regla_falsa_route():
    if request.method == "GET":
        return "<p>Regla falsa</p>"
    else:
        fx = request.get_json()["fx"]
        a = float(request.get_json()["a"])
        b = float(request.get_json()["b"])
        tol = float(request.get_json()["tol"])
        n_iter = float(request.get_json()["n_iter"])
        return regla_falsa.regla_falsa(
            fx, a, b, tol, n_iter
        )  # TODO: Check thath the method is correct


@app.route("/puntoFijo", methods=["GET", "POST"])
def punto_fijo_route():
    if request.method == "GET":
        return "<p>Punto fijo</p>"
    else:
        fx = request.get_json()["fx"]
        g = request.get_json()["g"]
        x0 = float(request.get_json()["x0"])
        tol = float(request.get_json()["tol"])
        n_iter = float(request.get_json()["n_iter"])
        return punto_fijo.pf(fx, g, x0, tol, n_iter)


@app.route("/newton", methods=["GET", "POST"])
def newton_route():
    if request.method == "GET":
        return "<p>Newton</p>"
    else:
        return jsonify(
            {
                "Result": "R",
            }
        )


@app.route("/secante", methods=["GET", "POST"])
def secante_route():
    if request.method == "GET":
        return "<p>secante</p>"
    else:
        return jsonify(
            {
                "Result": "R",
            }
        )


@app.route("/newton_mod1", methods=["GET", "POST"])
def newton_mod1_route():
    if request.method == "GET":
        return "<p>Newton mod 1</p>"
    else:
        return jsonify(
            {
                "Result": "R",
            }
        )


@app.route("/newton_mod2", methods=["GET", "POST"])
def newton_mod2_route():
    if request.method == "GET":
        return "<p>Newton mod 2</p>"
    else:
        return jsonify(
            {
                "Result": "R",
            }
        )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

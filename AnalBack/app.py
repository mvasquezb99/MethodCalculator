from flask import Flask, jsonify, request
from flask_cors import CORS
from metodos import biseccion

app = Flask(__name__)
cors = CORS(app, origins="*")


@app.route("/")
def home():
    return "<p>Home</p>"


@app.route("/biseccion", methods=["GET", "POST"])  # type: ignore
def biseccion_get():
    if request.method == "GET":
        return "<p>Biseccion</p>"
    else:
        fx = request.get_json()["fx"]
        a = float(request.get_json()["a"])
        b = float(request.get_json()["b"])
        tol = float(request.get_json()["tol"])
        n_iter = float(request.get_json()["n_iter"])
        return biseccion.bisec(fx, a, b, tol, n_iter)


@app.route("/reglaFalsa", methods=["GET", "POST"])
def regla_falsa_get():
    if request.method == "GET":
        return "<p>Regla falsa</p>"
    else:
        return jsonify(
            {
                "Result": "R",
            }
        )


@app.route("/puntoFijo", methods=["GET", "POST"])
def punto_fijo_get():
    if request.method == "GET":
        return "<p>Punto fijo</p>"
    else:
        return jsonify(
            {
                "Result": "R",
            }
        )


@app.route("/newton", methods=["GET", "POST"])
def newton_get():
    if request.method == "GET":
        return "<p>Newton</p>"
    else:
        return jsonify(
            {
                "Result": "R",
            }
        )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

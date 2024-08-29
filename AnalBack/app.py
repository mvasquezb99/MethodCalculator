from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Home</p>"


@app.route("/biseccion")
def biseccion():
    return "<p>Biseccion</p>"


@app.route("/reglaFalsa")
def regla_falsa():
    return "<p>Regla falsa</p>"


@app.route("/puntoFijo")
def punto_fijo():
    return "<p>Punto fijo</p>"


@app.route("/newton")
def newton():
    return "<p>Newton</p>"

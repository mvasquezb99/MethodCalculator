from flask import Flask, jsonify, request
from flask_cors import CORS
from metodos import (biseccion, biseccion2, mat_jacobi, mat_jacobi2,
                     mat_scidel, mat_scidel2, mat_sor, mat_sor2, mod1_newton,
                     mod1_newton2, mod2_newton, mod2_newton2, newton, newton2,
                     punto_fijo, punto_fijo2, regla_falsa, regla_falsa2,
                     secante, secante2)

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
                "tol": "",
                "n_iter": "",
                "explicacion": "El método de la bisección es un algoritmo matemático utilizado para encontrar una aproximación de la raíz de una función continua en un intervalo cerrado [a,b], donde se sabe que la función cambia de signo (es decir, f(a)⋅f(b)<0). El método se basa en la idea de dividir el intervalo en dos mitades, iterativamente, hasta que se encuentra un valor que se aproxime lo suficiente a la raíz de la ecuación.",
                "use_cs": "",  # if 1 then use relative error
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
                "tol": "",
                "n_iter": "",
                "explicacion": "El método de la regla falsa (o método de interpolación lineal) es otro algoritmo para encontrar una aproximación de la raíz de una función continua en un intervalo [a,b] donde f(a)⋅f(b)<0. A diferencia del método de la bisección, en el que el intervalo se divide por la mitad en cada paso, el método de la regla falsa usa una aproximación lineal de la función para determinar dónde se encuentra la raíz. Este método generalmente converge más rápido que el de la bisección, aunque puede ser menos estable en algunos casos.",
                "use_cs": "",  # if 1 then use relative error

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
                "tol": "",
                "n_iter": "",
                "explicacion": "El método del punto fijo es un algoritmo utilizado para encontrar una solución a una ecuación de la forma f(x)=0 al reformularla como una ecuación de punto fijo, es decir, x=g(x), donde g(x) es una función que, bajo ciertas condiciones, iterativamente se aproxima a una solución. El objetivo del método es encontrar un punto x∗ tal que x∗=g(x∗), lo que implica que x∗x∗ es un punto fijo de la función g.",
                "use_cs": "",  # if 1 then use relative error
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
                "tol": "",
                "n_iter": "",
                "explicacion": "El método de Newton (también llamado método de Newton-Raphson) es un algoritmo iterativo que se utiliza para encontrar aproximaciones de las raíces de una función f(x)=0. Este método es conocido por su rapidez de convergencia en comparación con otros métodos, como la bisección o la regla falsa, siempre que se inicie cerca de la raíz.",
                "use_cs": "",  # if 1 then use relative error
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
                "tol": "",
                "n_iter": "",
                "explicacion": "El método de la secante es un algoritmo numérico para encontrar aproximaciones de las raíces de una función f(x)=0. Este método es una variante del método de Newton, pero, a diferencia de Newton, no requiere el cálculo de la derivada de la función. En su lugar, el método de la secante utiliza una aproximación de la derivada mediante diferencias finitas, lo que lo hace más eficiente en ciertos casos donde calcular la derivada es complicado.",
                "use_cs": "",  # if 1 then use relative error
            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        x0 = float(request.get_json()["input"]["x0"])
        x1 = float(request.get_json()["input"]["x1"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return secante2.seca2(fx, x0, x1, tol, n_iter)
        return secante.seca(fx, x0, x1, tol, n_iter)


@app.route("/newton_mod1", methods=["GET", "POST"])
def newton_mod1_route():
    if request.method == "GET":
        return jsonify(
            {
                "fx": "",
                "x0": "",
                "m": "",
                "tol": "",
                "n_iter": "",
                "explicacion": "El método modificado de Newton para raíces múltiples es una variante del método de Newton que se utiliza cuando se quiere encontrar una raíz múltiple de una función. Una raíz múltiple ocurre cuando la función f(x) toca el eje xx pero no lo cruza, lo que significa que la derivada de la función también es cero en ese punto (o en parte de la vecindad de la raíz). Este tipo de raíces hace que el método de Newton convencional converja más lentamente o incluso falle, por lo que es necesario modificarlo.",
                "use_cs": "",  # if 1 then use relative error
            }
        )
    else:
        fx = request.get_json()["fx"]
        x0 = float(request.get_json()["input"]["x0"])
        m = float(request.get_json()["input"]["m"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return mod1_newton2.mnt(fx, m, x0, tol, n_iter)
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
                "n_iter": "",
                "explicacion": "El método modificado de Newton para raíces múltiples sin utilizar directamente la multiplicidad m es otra variante del método de Newton que ajusta el procedimiento iterativo sin necesidad de conocer o estimar la multiplicidad de la raíz. Esta modificación se basa en el uso tanto de la función f(x) como de su derivada primera f′(x) y segunda derivada f′′(x), lo que permite mejorar la convergencia hacia una raíz múltiple.",
                "use_cs": "",  # if 1 then use relative error

            }
        )
    else:
        fx = request.get_json()["input"]["fx"]
        x0 = float(request.get_json()["input"]["x0"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return mod2_newton2.mnt(fx, x0, tol, n_iter)
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
                "tol": "",
                "n_iter": "",
                "explicacion": "El método de Jacobi es un algoritmo iterativo utilizado para resolver sistemas de ecuaciones lineales de la forma Ax=b, donde A es una matriz de coeficientes, x es el vector de incógnitas y b es el vector de términos independientes. Este método es especialmente útil cuando la matriz AA es dispersa (tiene muchos ceros) o es diagonalmente dominante. El método de Jacobi es relativamente simple de implementar y puede ser utilizado en problemas de gran escala.",
                "use_cs": "",  # if 1 then use relative error
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
                "tol": "",
                "n_iter": "",
                "explicacion": "El método de Gauss-Seidel es un algoritmo iterativo para resolver sistemas de ecuaciones lineales de la forma Ax=b, similar al método de Jacobi. Sin embargo, el método de Gauss-Seidel mejora la velocidad de convergencia al utilizar los valores más recientes de las incógnitas dentro de cada iteración, lo que lo hace más eficiente en muchos casos. Es especialmente útil para sistemas con matrices grandes y dispersas o cuando se puede garantizar la convergencia.",
                "use_cs": "",  # if 1 then use relative error
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


@app.route("/mat_sor", methods=["GET", "POST"])
def mat_sor_route():
    if request.method == "GET":
        return jsonify(
            {
                "A": "",
                "b": "",
                "x0": "",
                "w": "",
                "use_cs": "",  # if 1 then use relative error
                "tol": "",
                "n_iter": "",
                "explicacion": "El método de Gauss-Seidel relajado o SOR (Successive Over-Relaxation) es una mejora del método de Gauss-Seidel para acelerar su convergencia mediante la introducción de un factor de relajación ω. Este factor ajusta cuánto de la nueva aproximación calculada en cada iteración debe ser utilizada. Dependiendo de la elección de ω, el método puede converger más rápidamente que el método estándar de Gauss-Seidel.",
            }
        )
    else:
        A = request.get_json()["input"]["A"]
        b = request.get_json()["input"]["b"]
        x0 = request.get_json()["input"]["x0"]
        w = float(request.get_json()["input"]["w"])
        tol = float(request.get_json()["input"]["tol"])
        n_iter = float(request.get_json()["input"]["n_iter"])
        if request.get_json()["input"]["use_cs"] == "1":
            return mat_sor2.mat_sor2(A, b, x0, tol, n_iter, w)
        else:
            return mat_sor.mat_sor(A, b, x0, tol, n_iter, w)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

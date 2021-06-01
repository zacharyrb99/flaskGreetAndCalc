from operations import add,sub,mult,div
from flask import Flask, request
app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b parameters."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)

    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract and b parameters."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def do_mult():
    """Multiply a and b parameters."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)

    return str(result)

@app.route("/div")
def do_div():
    """Divide a and b parameters."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)

    return str(result)

########################################
#shorter version
########################################
OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<operation>")
def math(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    answer = OPERATIONS[operation](a,b)

    return str(answer)

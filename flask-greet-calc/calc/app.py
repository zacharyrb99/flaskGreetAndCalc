from operations import add,sub,mult,div
from flask import Flask, request
app = Flask(__name__)


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

from flask import Flask

app = Flask(__name__)

# Index route
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


# Print string route
@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)  # prints to console
    return parameter  # displays in browser


# Count route
@app.route("/count/<int:parameter>")
def count(parameter):
    numbers = ""
    for i in range(parameter):
        numbers += f"{i}\n"
    return numbers


# Math route
@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation", 400

    return str(result)


if __name__ == "__main__":
    app.run(debug=True, port=5555)

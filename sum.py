from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("sum.html", result=None)

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        result = num1 + num2
        return render_template("sum.html", result=result)
    except ValueError:
        return render_template("sum.html", result="Invalid Input!")

if __name__ == "__main__":
    app.run(debug=True)

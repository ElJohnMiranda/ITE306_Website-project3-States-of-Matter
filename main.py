from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("page.html")


@app.route("/page")
def page():
    return render_template("page.html")


@app.route("/gas")
def gas():
    return render_template("gas.html")


@app.route("/liquid")
def liquid():
    return render_template("liquid.html")


@app.route("/solid")
def solid():
    return render_template("solid.html")


@app.route("/plasma")
def plasma():
    return render_template("plasma.html")


if __name__ == "__main__":
    app.run()

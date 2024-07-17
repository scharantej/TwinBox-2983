
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("main.html")

@app.route("/compare", methods=["POST"])
def compare():
    text1 = request.form["text1"]
    text2 = request.form["text2"]
    if text1 == text2:
        return render_template("result.html", result="success")
    else:
        return render_template("result.html", result="danger")

if __name__ == "__main__":
    app.run()

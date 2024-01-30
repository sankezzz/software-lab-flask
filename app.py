from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/name")
def hello():
    return "hello"

@app.route("/age")
def age():
    return "21"

@app.route("/batch")
def batch():
    return "B3"
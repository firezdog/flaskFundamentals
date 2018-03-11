from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninjaturtles.html")

@app.route('/ninja/<color>')
def color(color):
    return render_template("ninjaturtle.html", color=color)

app.run(debug=False)
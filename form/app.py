from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info", methods=["GET", "POST"])
def info():
    if request.method == "POST":
        global form
        form = request.form
        print type(form)
        return redirect("/info")
    if request.method == "GET":
        return render_template("info.html", form = form)

app.run(debug=True)
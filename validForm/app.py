from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = "notime"

@app.before_first_request
def init():
    session["validName"] = True
    session["validComment"] = True

@app.route("/")
def index():
    return render_template("index.html", form = session["form"], validName = session["validName"], validComment = session["validComment"])

@app.route("/info", methods=["GET", "POST"])
def info():
    if request.method == "POST":
        session["form"] = request.form
        return redirect("/info")
    if request.method == "GET":
        form = session["form"]
        if not len(form["name"]) > 0:
            session["validName"] = False
        else: session["validName"] = True
        if not len(form["comment"]) >= 120:
            session["validComment"] = False
        else: session["validComment"] = True
        if session["validName"] and session["validComment"]: return render_template("info.html", form = form)
        else: return redirect("/")

app.run(debug=True)
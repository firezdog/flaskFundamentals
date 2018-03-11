from flask import Flask, render_template, request, redirect
app = Flask(__name__)

set = False

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        global set
        global red
        global blue
        global green
        if not set:
            red = 0
            blue = 0
            green = 0
            set = True
        return render_template("index.html", red=red, blue=blue, green=green)
    else:
        red = request.form["red"]
        green = request.form["green"]
        blue = request.form["blue"]
        return redirect("/")
app.run(debug=True)
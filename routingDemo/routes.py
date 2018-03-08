from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")

def index():
    print("Loading index")
    return render_template("index.html")

@app.route("/success")

def success():
    return render_template("success.html")

@app.route("/users", methods=["POST"])

def create_user():
    print "Got Post Info"
    name = request.form["name"]
    email = request.form["email"]
    return redirect("/success")

app.run(debug=True)
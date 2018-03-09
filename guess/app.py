import random
from flask import Flask, session, render_template, request, redirect

app = Flask(__name__)                            
app.secret_key = "notimeforthat"

                               
@app.before_first_request
def init_app():
    session["result"] = ""
    session["class"] = ""
    session["random"] = random.randrange(0,101)
    print session["random"]

@app.route('/', methods=["GET", "POST"])  
def index():
    if request.method == "POST":
        if int(request.form["guess"]) == session["random"]:
            session["result"] = "Correct!"
            session["class"] = "correct"
            return redirect("/")
        else:
            if int(request.form["guess"]) < session["random"]:
                session["result"] = "Too low..."
                session["class"] = "incorrect"
            else:
                session["result"] = "Too high..."
                session["class"] = "incorrect"
            return redirect("/")
    else:
        return render_template("index.html")

@app.route('/reset', methods=["POST"])
def result():
    init_app()    
    return redirect("/")

app.run(debug=True)
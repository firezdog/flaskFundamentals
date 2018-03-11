from flask import Flask, session, render_template, request, redirect

app = Flask(__name__)                            
app.secret_key = "notimeforthat"

                               
@app.before_first_request
def init_app():
    session["sessions"] = 0

@app.route('/', methods=["GET", "POST"])  
def index():
    if request.method == "POST":
        print request.form['submit']
        if request.form['submit'] == "+2":
            session["sessions"] += 1
            return redirect("/")
        else:
            session["sessions"] = 0
            return redirect("/")
            
    else:
        session["sessions"] += 1
        return render_template("index.html")

app.run(debug=True)
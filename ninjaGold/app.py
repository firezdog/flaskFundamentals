from flask import Flask, render_template, request, redirect, jsonify
import random

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def main():
    if request.method=="GET":
        return render_template("index.html")
    else:
        building = request.form["building"]
        if building == "farm":
            gold = random.randrange(10,21)
            win = True
        elif building == "cave":
            gold = random.randrange(5,11)
            win = True
        elif building == "house":
            gold = random.randrange(2,6)
            win = True
        else:
            gold = random.randrange(0,51)
            win = random.randrange(0,2)
        return jsonify(activity=building,win=win,gold=gold)

app.run(debug=True)
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/ajax")
def ajax():
    print request.args
    response = request.args["color"]
    if response == "red":
        return jsonify(turtle="Raphael", image="static/Ninjas/raphael.jpg")
    elif response == "blue":
        return jsonify(turtle="Leonardo", image="static/Ninjas/leonardo.jpg")
    elif response == "orange":
        return jsonify(turtle="Michelangelo", image="static/Ninjas/michelangelo.jpg")
    elif response == "purple":
        return jsonify(turtle="Donatello", image="static/Ninjas/donatello.jpg")
    else:
        return jsonify(turtle="someone else", image="static/Ninjas/notapril.jpg")

app.run(debug=True)
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template("user.html", name = username)
app.run(debug=False)
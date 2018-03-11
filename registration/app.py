from flask import Flask, request, render_template, redirect, session, flash
import re
import datetime

app = Flask(__name__)
app.secret_key = "..."

emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
pwdRegex = re.compile(r'(?=.*[A-Z])(?=.*[0-9])')
bdayRegex = re.compile(r'\d{1,2}\/\d{1,2}\/\d{4}')

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        credentials = checkCredentials(request.form)
        passed = True
        for cred in credentials:
            if not credentials[cred]:
                passed = False
        if passed:
            return render_template("success.html")
        else:
            getErrors(credentials)
            return redirect('/')
    else:
        return render_template("index.html")

def checkCredentials(form):
    credentials = {
        "email": False,
        "longFirst": False,
        "alphaFirst": False,
        "longLast": False,
        "alphaLast": False,
        "birthday": False,
        "earlier": False,
        "passwordLength": False,
        "passwordMatch": False,
        "passwordForm": False
    }
    credentials["longFirst"], credentials["alphaFirst"] = checkName(form["first"])
    credentials["longLast"], credentials["alphaLast"] = checkName(form["last"])
    credentials["birthday"], credentials["earlier"] = checkBirthday(form["birthday"])
    credentials["passwordLength"], credentials["passwordMatch"], credentials["passwordForm"] = checkPassword(form["password"], form["confirm_password"])
    credentials["email"] = checkEmail(form["email"])
    return credentials

def getErrors(credentials):
    if not credentials["longFirst"]:
        flash("First name cannot be blank.")
    elif not credentials["alphaFirst"]:
        flash("First name cannot contain numbers or other special characters.")
    if not credentials["longLast"]:
        flash("Last name cannot be blank.")
    elif not credentials["alphaLast"]:
        flash("Last name cannot contain numbers or other special characters.")
    if not credentials["birthday"]:
        flash("Invalid date or incorrect format.")
    elif not credentials["earlier"]:
        flash("You must have been born yesterday, at least.")
    if not credentials["passwordLength"]:
        flash("Password must be at least 8 characters in length.")
    elif not credentials["passwordForm"]:
        flash("Password must contain one capital letter and one number.")
    if not credentials["passwordMatch"]:
        flash("Password and password confirmation do not match.")
    if not credentials["email"]:
        flash("Invalid e-mail.")

def checkBirthday(birthday):
    match = False
    earlier = False
    if bdayRegex.match(birthday):
        now = datetime.datetime.now()
        then = birthday.split("/")
        then = map(int, then)
        today = [now.month,now.day,now.year]
        #Check to see if date exists.
        if then[0] < 13:
            if then[0] in [1,3,5,7,8,10,12]:
                if then[1] in range(1,32):
                    match = True
            if then[0] in [4,6,9,11]:
                if then[1] in range(1,31):
                    match = True
            #Ugh, February...
            if then[0] == 2:
                #If it's not divisible by 4, it's a common year.
                if not then[2] % 4 == 0:
                    if then[1] in range(1,29): match = True
                #Otherwise it's a leap year...if it's not divisible 100...
                elif not then[2] % 100 == 0:
                    if then[1] in range(1,30): match = True
                #...if it is divisible by 100, it's a common year...
                elif not then[2] % 400 == 0:
                    if then[1] in range(1,29): match = True
                #...unless it's also divisible by 400 (whew)
                else:
                    if then[1] in range(1,30): match = True
        #If the year is greater than the year entered, the date entered is earlier.
        if today[2] > then[2]:
            earlier = True
        #Otherwise, if the year is the same as the year entered...
        elif today[2] == then[2]:
        #...and the month is later than the month entered, the date entered is earlier.
            if today[0] > then[0]:
                earlier = True
            #Otherwise, if the month is the same as the month entered...
            elif today[0] == then[0]:
                #...and the day is greater than the day entered, the date entered is earlier.
                if today[1] > then[1]:
                    earlier = True
    return match, earlier

def checkEmail(email):
    if emailRegex.match(email):
        return True

def checkName(name):
    longName, alphaName = False, False
    if len(name) > 0:
        longName = True
    if name.isalpha():
        alphaName = True
    return longName, alphaName

def checkPassword(pwd, pwdconf):
    passwordLength, passwordMatch, passwordForm = False, False, False
    if len(pwd) > 7:
        passwordLength = True
    if pwd == pwdconf:
        passwordMatch = True
    if pwdRegex.match(pwd):
        passwordForm = True
    return passwordLength, passwordMatch, passwordForm

app.run(debug=True)
from flask import Flask

"""
The variable __name__ is passed as first argument when creating an instance of the Flask object (a Python Flask application). 
In this case __name__ represents the name of the application package and it’s used by Flask to identify resources liketemplates,static assets and the instance folder.
"""
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/profile/<userId>")
def showProfile(userId):
    return "Profile -> UserId: {}".format(userId)

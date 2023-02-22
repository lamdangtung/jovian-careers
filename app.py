from flask import Flask, render_template, jsonify

"""
The variable __name__ is passed as first argument when creating an instance of the Flask object (a Python Flask application). 
In this case __name__ represents the name of the application package and it’s used by Flask to identify resources liketemplates,static assets and the instance folder.
"""
app = Flask(__name__)

jobs = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "Rs. 15,000,000"
    },
    {
        "id": 2,
        "title": "Front Engineer",
        "location": "Remote",
        "salary": "Rs. 2,000,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Delhi, India",
        "salary": "Rs. 50,000,000"
    },
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "LA, USA",
    },
]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=jobs, company_name="Jovain")


@app.route("/api/jobs")
def get_job_list():
    return jsonify(jobs)


@app.route("/profile/<userId>")
def showProfile(userId):
    return "Profile -> UserId: {}".format(userId)

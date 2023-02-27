from flask import Flask, render_template, jsonify
from database import getAllJobs, getJobById
import json
"""
The variable __name__ is passed as first argument when creating an instance of the Flask object (a Python Flask application). 
In this case __name__ represents the name of the application package and it’s used by Flask to identify resources liketemplates,static assets and the instance folder.
"""
app = Flask(__name__)


@app.route("/")
def show_home_page():
    jobs = getAllJobs()
    return render_template('home.html', jobs=jobs, company_name="Jovain")


@app.route("/job/<jobId>")
def show_detail_job_page(jobId):
    job = getJobById(jobId)
    return render_template('job_detail.html', job=job)

# API


@app.route("/api/job/<jobId>")
def get_job_by_id(jobId):
    job = getJobById(jobId)
    return jsonify(job)


@app.route("/api/jobs")
def get_job_list():
    jobs = getAllJobs()
    return jsonify(jobs)

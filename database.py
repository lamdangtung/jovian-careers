import os
import pymysql
import json
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
database = os.getenv("DATABASE")
ssl_cert = os.getenv("SSL_CERT")

connection_string = "mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8mb4".format(
    username, password, host, database)

engine = create_engine(connection_string)

conn = engine.connect()


def getAllJobs():
    sql_query = "select * from jobs"
    result = conn.execute(text(sql_query))
    jobs = []
    for row in result.fetchall():
        jobs.append(row._asdict())
    return jobs


def getJobById(jobId):
    result = conn.execute(
        text("select * from jobs where id =:id"), {"id": jobId})
    rows = result.fetchall()
    if (rows.count == 0):
        return None
    else:
        return rows[0]._asdict()


def addApplication(application, jobId):
    query = text("insert into applications (job_id,full_name,email,linkedin_url,education,work_experience,resume_url) values (:job_id,:full_name,:email,:linkedin_url,:education,:work_experience,:resume_url)")
    conn.execute(query, {
        "job_id": jobId,
        "full_name": application['full_name'],
        "email": application['email'],
        "linkedin_url": application['linkedin_url'],
        "education": application['education'],
        "work_experience": application['work_experience'],
        "resume_url": application['resume_url']
    })

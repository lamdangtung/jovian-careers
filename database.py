import os
import pymysql
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
    result_dicts = []
    for row in result:
        result_dicts.append(row._mapping)
    return result_dicts

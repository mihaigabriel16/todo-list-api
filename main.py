from flask import *
import json 
import sqlite3


app = Flask(__name__)


if __name__ == '__main__':
    app.run(port=8888)


def go_home():
    c = sqlite3.connect("student.db").cursor()
    c.execute("CREATE TABLE IF NOT EXISTS STUDENTS(""id TEXT, firstname TEXT, lastname TEXT, department TEXT)")
    c.connection.close()


class Student:
    def __init__(self) -> None:
        pass
import os
import sqlite3 as sql
import hashlib
import base64
from flask import Flask, flash, redirect, render_template, request, make_response

app = Flask(__name__)


path = os.path.join(os.path.dirname(__file__),'users.db')

def connect_database():
    return sql.connect(path)

def get_user(username, password):
    database = connect_database()
    cursor = database.cursor()
    try:
        cursor.execute('SELECT username, password FROM `users` WHERE username=\'%s\' AND password=\'%s\'' % (username, hashlib.md5(password.encode()).hexdigest()))
    except Exception as e:
        return -99
    row = cursor.fetchone()
    database.commit()
    database.close()
    if row is None: 
        return None
    return (row[0], row[1])

@app.route("/")
def root():
    response = make_response(render_template("login.html"))
    cookie_string = 'md5 but make sure to delete this later!!!'
    cookie_string = base64.b64encode(base64.b64encode(cookie_string.encode('ascii')))
    response.set_cookie('encoding', cookie_string)
    return response

@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if '-' in username or '#' in username or '*' in username or '/' in username:
        return render_template("sqli_detected.html")
    if 'or' in username.lower() or 'or' in password.lower() or '|' in username.lower() or '|' in password.lower():
        return render_template("sqli_detected.html")
    if 'and' in username.lower() or 'and' in password.lower() or '&' in username.lower() or '&' in password.lower():
        return render_template("sqli_detected.html")
    if 'UNION' in username or 'SELECT' in username or 'FROM' in username:
        return render_template("sqli_detected.html")

    result = get_user(username, password)

    if result == -99:
        return render_template("error.html")

    if result != None:
        return render_template("success.html")

    return render_template("failure.html")

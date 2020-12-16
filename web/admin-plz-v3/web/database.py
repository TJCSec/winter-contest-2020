
import os
import sqlite3 as sql
from flask import Flask, flash, redirect, render_template, request

path = os.path.join(os.path.dirname(__file__),'users.db')

def connect_database():
    return sql.connect(path)
    
def setup_database():
    database = connect_database()
    cursor = database.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50),
            password VARCHAR(50)
            )''')
    users = [('admin','13831de1c5819a2b716204f1e083fe34')]
    cursor.executemany('INSERT INTO `users` VALUES(NULL, ?,?)',users)
    database.commit()
    database.close()

def init():
    setup_database()

init()

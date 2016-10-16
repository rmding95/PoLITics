from collections import Counter

from flask import Flask, request, g, url_for
from flask.ext.api import FlaskAPI, status, exceptions

import csv
import sqlite3
    
DATABASE = '/var/www/html/flaskapp/tweets.db'

def connect_to_database():
    return sqlite3.connect(app.config['DATABASE'])

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def execute_query(query, args=()):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

cursor.execute("SELECT COUNT(*) from result where server_state='2' AND name LIKE '"+digest+"_"+charset+"_%'")
result=cursor.fetchone()
number_of_rows=result[0]
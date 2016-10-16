from flask import Flask, request, g, url_for
from flask.ext.api import FlaskAPI, status, exceptions

import csv
import sqlite3
    
DATABASE = '/var/www/html/flaskapp/natlpark.db'

app = FlaskAPI(__name__)
app.config.from_object(__name__)



##### CONNECT TO DATABASE #####

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



##### ENDPOINTS #####

@app.route("/viewdb")
def viewdb():
    rows = execute_query("""SELECT * FROM natlpark""")
    return rows

@app.route('/data')
def get_data():
    return {"x": "123", "y": "456", "party": "republican"}


if __name__ == '__main__':
    app.run()
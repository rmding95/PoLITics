from flask import Flask, request, g, url_for
from flask.ext.api import FlaskAPI, status, exceptions
import boto3

app = FlaskAPI(__name__)
app.config.from_object(__name__)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tweets')

<<<<<<< HEAD
@app.route("/viewdb")
def viewdb():
    response = table.scan()
    data = response['Items']
    return data
=======
##### CONNECT TO DATABASE #####

def connect_to_database():
    return sqlite3.connect('tweets.db')

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
    cur = get_db().execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows
>>>>>>> origin/master



##### ENDPOINTS #####

GUIDE = ['x', 'y', 'party', 'tweet_time']



@app.route('/data')
def get_data():
    return {"x": "123", "y": "456", "party": "republican"}


if __name__ == '__main__':
    # db.create_all()
    app.run()
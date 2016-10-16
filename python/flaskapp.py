from flask import Flask, request, g, url_for
from flask.ext.api import FlaskAPI, status, exceptions
import boto3

app = FlaskAPI(__name__)
app.config.from_object(__name__)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tweets')

@app.route("/viewdb")
def viewdb():
    response = table.scan()
    data = response['Items']
    return data



##### ENDPOINTS #####

GUIDE = ['x', 'y', 'party', 'tweet_time']



@app.route('/data')
def get_data():
    return {"x": "123", "y": "456", "party": "republican"}


if __name__ == '__main__':
    # db.create_all()
    app.run()
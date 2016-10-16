from flask import Flask, jsonify
import os
import boto3

from boto.dynamodb2.table import Table

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/test', methods=['GET'])
def test():
    return "test"

@app.route('/data', methods=['GET'])
def data():
	dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='https://dynamodb.us-west-2.amazonaws.com')
	table = dynamodb.Table('Tweets')
	response = table.scan()
	data = response['Items']
	return jsonify(data)

if __name__ == '__main__':
    app.run()
from flask import Flask
import os

from boto.dynamodb2.table import Table

app = Flask(__name__)
# app.config['DYNAMO_TABLES'] = [
#     Table('Tweets', schema=[HashKey('ID')])
# ]

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/test', methods=['GET'])
def test():
    return "test"

@app.route('/data', methods=['GET'])
def data():
	return "data"

if __name__ == '__main__':
    app.run()
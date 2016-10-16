from flask import Flask
import os
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAIXQBGVZZ5R56OM2A'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'

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
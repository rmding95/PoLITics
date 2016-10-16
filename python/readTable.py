import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tweets')

def read():
	response = table.scan()
	data = response['Items']
	return data
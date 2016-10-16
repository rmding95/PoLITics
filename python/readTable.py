import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('Tweets')

def read():
	response = table.scan()
	data = response['Items']
	return data
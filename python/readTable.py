import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tweets')

response = table.scan()
data = response['Items']

print data
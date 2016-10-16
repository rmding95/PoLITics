import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='Tweets',
    KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
    	{
            'AttributeName': 'ID',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'lat',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'long',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'party',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'time',
            'AttributeType': 'S'
        }

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
import boto3
import json

# Create an instance of the DynamoDB client
dynamodb = boto3.client('dynamodb', aws_access_key_id='aws_access_key', aws_secret_access_key='aws_secret_key',region_name='aws_region')

# # Connect to DynamoDB
# dynamodb = dynamodb.resource('dynamodb')
# client = dynamodb.client('dynamodb')

# Define the table name
table_name = 'songs'

# Read the JSON file
with open('songs.json', 'r') as file:
    data = json.load(file)


# table = dynamodb.Table('songs')  # Replace 'YourTableName' with the actual table name in DynamoDB

# Create items in DynamoDB
for item in data['data']:
    dynamodb.put_item(TableName=table_name, Item=item)

print('Items created successfully.')

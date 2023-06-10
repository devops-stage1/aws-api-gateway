import boto3
import json

def lambda_handler(event, context):

    query_string = event.get('queryStringParameters')
    
    if query_string is not None:
    
        song_name = query_string['q']
        
        song_name = song_name.title()

        # Create an instance of the DynamoDB client
        dynamodb = boto3.client('dynamodb')
    
        # Define the table name
        table_name = 'songs'  # Replace 'YourTableName' with the actual table name in DynamoDB
    
        # Retrieve an item from the table
        response = dynamodb.get_item(
            TableName=table_name,
            Key={
                'name': {'S': song_name}
            }
        )

        # Process the retrieved item
        item = response['Item']
    else:
        item = {
            "message": "Nothing found"
        }
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(item) 
    }

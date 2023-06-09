import boto3

# # Create an instance of the DynamoDB client
dynamodb = boto3.client('dynamodb', aws_access_key_id='aws_access_key', aws_secret_access_key='aws_secret_key',region_name='aws_region')

# # # Connect to DynamoDB
# # dynamodb = dynamodb.resource('dynamodb')
# # client = dynamodb.client('dynamodb')

# Define the table schema
table_name = 'songs'  # Replace 'YourTableName' with the desired table name
attribute_definitions = [
    {
        'AttributeName': 'name',
        'AttributeType': 'S'
    }
]
key_schema = [
    {
        'AttributeName': 'name',
        'KeyType': 'HASH'
    }
]
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}


# Create the table
table = dynamodb.create_table(
    TableName=table_name,
    AttributeDefinitions=attribute_definitions,
    KeySchema=key_schema,
    ProvisionedThroughput=provisioned_throughput
)

print('Table created successfully.')


import boto3

# Create an instance of the DynamoDB client
dynamodb = boto3.client('dynamodb', aws_access_key_id='aws_access_key', aws_secret_access_key='aws_secret_key',region_name='aws_region')


# Define the table name
table_name = 'songs'

# Define the key attribute(s) to identify the item to be updated
key = {
    'name': {'S': 'Hold On'}
}

# Define the attribute(s) to be updated
update_expression = 'SET #attr1 = :val1'
expression_attribute_names = {'#attr1': 'artist'}
expression_attribute_values = {':val1': {'S': 'Sasi Singh'}}

# mutiple attribute definition
# update_expression = 'SET #attr1 = :val1, #attr2 = :val2'
# expression_attribute_names = {'#attr1': 'Title', '#attr2': 'Description'}
# expression_attribute_values = {':val1': {'S': 'New Title'}, ':val2': {'S': 'New Description'}}

# Update the item
response = dynamodb.update_item(
    TableName=table_name,
    Key=key,
    UpdateExpression=update_expression,
    ExpressionAttributeNames=expression_attribute_names,
    ExpressionAttributeValues=expression_attribute_values
)

print("Item updated successfully!", response)

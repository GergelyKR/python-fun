import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('employees ')

resp = table.get_item(
    Key={
        'emp_id': 'catb'
    }
)

print=(resp['Item'])

table.delete_item(
    Key={
        'emp_id': 'catb'
    }
)
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('employees')

table.put_item(
    Item={
        'emp_id': 'catb',
        'Name': "Big Cat",
        'Location': "Berlin",
        'Info': {
            'Hobbies': 'Chasing mouse',
            'Marital Status': "Married"
        }
    }
)
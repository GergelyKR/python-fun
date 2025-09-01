# Need to configure IAM roles so the services can communicate
# Need to create EventBridge rule to trigger the script upon S3 upload

''' Example uploaded CSV
1,Jerry,Boston
2,Dexter,Washington
3,Mark,London
'''

import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees') # replace with your table name

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name = event['Records'][0]['s3']['object']['key']
    resp = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    data = resp['Body'].read().decode('utf-8')
    employees = data.split('\n')

    for emp in employees:
        print(emp)
        emp_data = emp.split(',')
        # Persist data in DynamoDB
        try:
            table.put_item(
                Item={
                    'emp_id': emp_data[0],
                    'name': emp_data[1],
                    'location': emp_data[2]
                }
            )
        except Exception as e:
            print("End of file")
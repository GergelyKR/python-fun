# Need to configure IAM roles so the services can communicate
# Need to create EventBridge rule to trigger the script upon S3 upload

''' Example uploaded JSON:
{
    "emp_id":"4"
    "Name":"Geri"
    "Age":26,
    "Location":"USA"
}
'''

import boto3
import json
s3_client = boto3.client('s3')
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket, Key=json_file_name)
    jsonFileReader =json_object['Body'].read()
    jsonDict = json.loads(jsonFileReader)
    table = dynamodb.Table('employees') # replace with your table name
    table.put_item(Item=jsonDict)

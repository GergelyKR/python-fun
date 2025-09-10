# Requirements
# IAM role for Lambda function (and policy)

import boto3
import os

FROM_MAIL = os.environ(['FROM_MAIL'])
TO_MAIL = os.environ(['TO_MAIL'])

ec2_client = boto3.client('ec2')
ses_client = boto3.client('ses')

def lambda_handler(event, context):
    response = ec2_client.describe_addresses()
    unused_eips = []
    for address in response['Addresses']:
        if 'InstanceId' not in address:
            unused_eips.append(address['PublicIp'])

    print(unused_eips)

    response = ses_client.send_email(
        Source=FROM_MAIL,
        Destination={
            'ToAddresses': [
                TO_MAIL,
            ]
        },
        Message={
            'Subject': {
                'Data': 'Unused Elastic IP addresses',
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': '\n'.join(unused_eips),
                    'Charset': 'UTF-8'
                }
            }
        }
    )
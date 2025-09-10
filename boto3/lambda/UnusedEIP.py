# Requirements
# IAM role for Lambda function (and policy)

import boto3

ec2_client = boto3.client('ec2')
ses_client = boto3.client('ses')


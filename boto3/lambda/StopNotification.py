# Needs IAM role, SNS topic and CloudWatch event to notify about the EC2 stop

import boto3
import os

client = boto3.client('sns')
TOPIC_ARN = os.environ['TOPIC_ARN']

def lambda_handler(event, context):
    topic_arn = TOPIC_ARN
    message = "Production server stopped, please check."
    client.publish(
        TopicArn = topic_arn,
        Subject = 'Server stopped',
        Message = message)
# Requirements:
# "Tags.json" file in target S3 bucket
# CloudTrail logs to S3
# IAM role for Lambda function (access S3, create tags)
# EventBridge rule to monitor instance creation (AWS API Call via CloudTrail) -> Specific event type (RunInstances) -> Target Lambda function

import json
import boto3
import os

s3 = boto3.client('s3')
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    try:
        # Extra instance ID from the event
        instance_id = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
        
        # S3 bucket and object details
        bucket_name = os.environ(['BUCKET_NAME'])
        object_key = 'tags.json'
        local_file_path = '/tmp/tags.json'
        
        # Download tags.json from S3
        s3.download_file(bucket_name, object_key, local_file_path)
        print(f"Downloaded {object_key} from {bucket_name} to {local_file_path}")

        # Read the tags.json file
        with open(local_file_path, 'r') as file:
            tags = json.load(file)
            print(f"Loaded tags from {local_file_path}")

        # Apply tags to the instance
        ec2.create_tags(Resources=[instance_id], Tags=tags)
        print(f"Applied tags to instance {instance_id}")

    except Exception as e:
        print(f"Error: {e}")
        return {"statusCode": 500, "body": "Error applying tags"}
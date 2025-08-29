import requests
import json
# import os

# External dependencies (libraries) need to be included in the package file uploaded to Lambda

slack_web_hook = input("Enter your Slack Webhook URL: ")
# slack_web_hook = os.environ['SLACK_WEB_HOOK'] -> If we use environment variable
# environment variables can also be encrypted with KMS and decrypted inside the function

def send_slack(event, context):
    print(str(event))
    slack_message = {"text": "EC2 Instance Stopped."}
    resp = requests.post(slack_web_hook, data=json.dumps(slack_message))
    return resp.text
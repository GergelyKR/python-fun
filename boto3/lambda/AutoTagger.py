# Requirements:
# "Tags.json" file in target S3 bucket
# CloudTrail logs to S3
# IAM role for Lambda function (access S3, create tags)
# EventBridge rule to monitor instance creation (AWS API Call via CloudTrail) -> Specific event type (RunInstances) -> Target Lambda function

import json
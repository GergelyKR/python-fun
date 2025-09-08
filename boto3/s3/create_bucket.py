import boto3

client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='aws-geri-test-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-central-1'
    }
)
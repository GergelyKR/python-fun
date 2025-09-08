import boto3

client = boto3.client('s3')

response = client.delete_object(
    Bucket='aws-geri-test-bucket',
    Key='create_bucket.py'
)
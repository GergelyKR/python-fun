import boto3

client = boto3.client('s3')

response = client.list_objects(
    Bucket='aws-geri-test-bucket'
)

for obj in response['Contents']:
    print(obj['Key'])
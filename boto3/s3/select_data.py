import boto3

client = boto3.client('s3')

resp = client.select_object_content(
    Bucket='aws-geri-test-bucket',
    Key='files/employees.csv',
    Expression='Select s.name, s.email from S3Object s',
    ExpressionType='SQL',
    InputSerialization={
        'CSV': {
            'FileHeaderInfo': 'Use'
        }
    },
    OutputSerialization={
        'CSV': {
        }
    }
)

# Loop through payload object

for event in resp['Payload']:
    if 'Records' in event:
        print(event['Records']['Payload']).decode('utf-8')
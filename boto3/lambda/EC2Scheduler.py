# Start instance at 9:00 AM
# Stop instance at 6:00 PM
# Condition: Instances with tag key="Type" and Value ="Scheduled"
# Condition: Monday to Friday
# Related IAM roles have to be configured for Lambda
# Start and stop event can be triggered by CloudWatch

import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    filter = [
        {
            'Name': 'tag:Type',
            'Values': ['Scheduled']
        }
    ]
    instances = ec2.instances.filter(Filters=filter)

    for instance in instances:
        if instance.state['Name'] == 'running':
            instance.stop()
        elif instance.state['Name'] == 'stopped':
            instance.start()

    return {
        'statusCode': 200,
        'body': 'EC2 instances have been started / stopped.'
    }
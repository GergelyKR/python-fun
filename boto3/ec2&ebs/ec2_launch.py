import boto3
client = boto3.client('ec2')

resp = client.run_instances(ImageId='ami-05a2d2d0a1020fecd',
                     InstanceType='t2.micro',
                     MinCount=1,
                     MaxCount=1)
for instance in resp['Instances']: # filter ID from the response dict
    print(instance['InstanceId'])
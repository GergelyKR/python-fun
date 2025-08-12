import boto3

client = boto3.client('ec2')

print("Instance list of the account:")
resp = client.describe_instances()
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}, current status: {instance['State']['Name']}")

# Print if there are no instances:
if len(resp['Reservations']) == 0:
    print("No instances found.")

# Filtering state
print("Instances in \"running\" state:")
resp = client.describe_instances(Filters=[
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
])
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}")

# Filtering tags
print("Instances with \"Prod\" tag:")
resp = client.describe_instances(Filters=[
    {
        'Name': 'tag:Environment',
        'Values': ['Prod']
    }
])
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}")
import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    print(f"Instance ID: {instance.id} and instance type is {instance.instance_type}")

for instance in ec2.instances.filter(Filters=[ # Use filter for AZ
    {
        'Name': 'availability-zone',
        'Values': ['eu-central-1b']
    }
]):
    print(f"Instance ID: {instance.id} and instance type is {instance.instance_type}")

for instance in ec2.instances.filter(Filters=[ # Use filter for state
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
]):
    print(f"Instance ID: {instance.id} and instance type is {instance.instance_type}")


# Filter for running instances and calling stop method
ec2 = boto3.resource('ec2')
ec2.instances.filter(Filters=[
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
]).stop()
print("All running instances have been stopped.")
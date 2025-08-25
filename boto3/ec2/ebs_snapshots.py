import boto3

ec2 = boto3.resource('ec2')
sns_client = boto3.client('sns')

SNS_TOPIC_ARN = input("Enter the SNS topic ARN: ")

backup_filter = [
    {
        'Name': 'tag:Backup',
        'Values': ['Yes']
    }
]
snapshot_ids = []

# looping through List(ec2.Instance)
for instance in ec2.instances.filter(Filters=backup_filter):
    for vol in instance.volumes.all():
        snapshot = vol.create_snapshot(Description='Created by Boto3')
        snapshot_ids.append(snapshot.snapshot_id)

sns_client.publish(
    TopicArn = SNS_TOPIC_ARN,
    Subject = 'EBS Snapshots',
    Message = str(snapshot_ids)
)
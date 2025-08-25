# Delete snapshots older than 15 days

from datetime import datetime, timedelta, timezone

import boto3
ec2 = boto3.resource('ec2')

# List (ec2.Snapshot)
snapshots = ec2.snapshots.filter(OwnerIds=['self'])

for snapshot in snapshots:
    start_time = snapshot.start_time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days=15)
    if delete_time > start_time:
        snapshot.delete()
        print(f"The snapshot {snapshot.id} has been deleted.")
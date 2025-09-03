# Remove unused AMIs
# AMIs that are not attached to any instance
# AMIs that are older than 30 days

import boto3
client = boto3.client('ec2')

instances = client.describe_instances()
used_amis = []
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])

# Remove duplicate AMIs
def remove_duplicates(amis):
    unique_amis = []
    for ami in amis:
        if ami not in unique_amis:
            unique_amis.append(ami)
    return unique_amis

unique_amis = remove_duplicates(used_amis)
print(unique_amis)

# Get custom AMIs from account

custom_images = client.describe_images(
    Filters=[
            {   
            'Name': 'state',
            'Values': ['available']
            },
        ],
    Owners= ['self']
)

custom_amis_list = []
for image in custom_images['Images']:
    custom_amis_list.append(image['ImageId'])

for custom_ami in custom_amis_list:
    if custom_ami not in unique_amis:
        print(f"Deleting AMI: {custom_ami}")
        client.deregister_image(ImageId=image['ImageId'])
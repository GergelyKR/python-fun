# Functions to create or delete EBS volumes

# List all volumes
def ListVolumes():
    import boto3

    ec2_client = boto3.client('ec2')

    volumes = ec2_client.describe_volumes()
    if len(volumes['Volumes']) == 0:
        print("No volumes found.")
    else:
        for volume in volumes['Volumes']:
            print(f"VolumeId: {volume['VolumeId']}")
            print("----"*5)

def CreateVolumes():
    import boto3

    ec2_client = boto3.client('ec2')

    volumes = ec2_client.create_volume(
        AvailabilityZone='eu-central-1a',
        Size=8
    )
    print(f"Volume {volumes['VolumeId']} has been created.")

def DeleteVolumes():
    import boto3

    ec2_client = boto3.client('ec2')

    volumes = ec2_client.describe_volumes()
    for volume in volumes['Volumes']:
        if volume['State'] == 'available':
            ec2_client.delete_volume(VolumeId=volume['VolumeId'])
            print(f"Volume {volume['VolumeId']} has been deleted.")

def main():
    operation = input("Select the desired operation: \n1. List Volumes\n2. Create Volumes\n3. Delete All Volumes\n4. Exit\n")

    if operation == '1':
        ListVolumes()
        print("----"*5)
        main()
    elif operation == '2':
        CreateVolumes()
        print("----"*5)
        main()
    elif operation == '3':
        DeleteVolumes()
        print("----"*5)
        main()
    elif operation == '4':
        exit()
    else:
        print("Invalid input.")
        print("----"*5)
        main()

if __name__ == "__main__":
    main()
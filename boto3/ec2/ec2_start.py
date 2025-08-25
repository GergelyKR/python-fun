import boto3
client = boto3.client('ec2')

id = input("Enter the instance ID: ")
status_change = input("What would you like to do? Start/Stop/Terminate:")

if status_change == "Start":
    resp = client.start_instances(InstanceIds=[id])
    if resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print(f"The instance {id} has been started.")
    else:
        print(f"The instance {id} could not be started.")

elif status_change == "Stop":
    resp = client.stop_instances(InstanceIds=[id])
    if resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print(f"The instance {id} has been stopped.")
    else:
        print(f"The instance {id} could not be stopped.")
elif status_change == "Terminate":
    resp = client.terminate_instances(InstanceIds=[id])
    if resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print(f"The instance {id} has been terminated.")
    else:
        print(f"The instance {id} could not be terminated.")
else:
    print("Invalid input.")
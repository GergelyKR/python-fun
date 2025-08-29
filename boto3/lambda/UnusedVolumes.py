import boto3

ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

volumes = ec2_client.describe_volumes()
# for volume in volumes['Volumes']: -> List all volumes (dict, you can filter specific attributes)
#     print(volume)

sns_arn = input("Enter the SNS topic ARN: ")

def lambda_handler(event, context):
    unused_vols = []
    size = 0
    for volume in volumes['Volumes']:
        if len(volume['Attachments']) == 0:
            unused_vols.append(volume['VolumeId'])
            size = size + volume['Size']
            # print(volume)
            # print("----"*5)

    email_body = "##### Unused Volumes #####\n"

    for vol in unused_vols:
        email_body = email_body + f"VolumeId = {vol}\n"

    # send e-mail

    email_body = email_body + f"Total Size = {size} GB"

    sns_client.publish(
        TopicArn = sns_arn,
        Subject = 'Unused Volumes',
        Message = email_body
    )

    # print(email_body)
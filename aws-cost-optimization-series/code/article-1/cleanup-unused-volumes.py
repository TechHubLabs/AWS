import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    # Find unattached EBS volumes tagged "Environment=Dev"
    volumes = ec2.describe_volumes(Filters=[
        {'Name': 'status', 'Values': ['available']},
        {'Name': 'tag:Environment', 'Values': ['Dev']}
    ])
    
    # Delete unused volumes
    for vol in volumes['Volumes']:
        ec2.delete_volume(VolumeId=vol['VolumeId'])
        print(f"Deleted {vol['VolumeId']}")
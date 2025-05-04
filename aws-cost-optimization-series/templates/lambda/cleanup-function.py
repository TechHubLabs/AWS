import boto3
import os

def lambda_handler(event, context):
    region = os.environ.get('AWS_REGION', 'us-east-1')
    ec2 = boto3.client('ec2', region_name=region)
    
    # Stop instances without "Production" tag running over 24h
    instances = ec2.describe_instances(Filters=[
        {'Name': 'tag:Environment', 'Values': ['Dev', 'Test']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]).get('Reservations', [])
    
    instance_ids = [i['InstanceId'] for r in instances for i in r['Instances']]
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f"Stopped instances: {instance_ids}")
    return {"statusCode": 200, "body": "Cleanup completed"}
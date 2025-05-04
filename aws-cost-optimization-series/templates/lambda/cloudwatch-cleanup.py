import boto3
from datetime import datetime, timedelta

def delete_old_logs():
    logs = boto3.client('logs')
    cutoff = int((datetime.now() - timedelta(days=90)).timestamp() * 1000)
    
    groups = logs.describe_log_groups()['logGroups']
    for group in groups:
        if 'RetentionInDays' not in group:  # Never expire logs
            logs.delete_log_group(logGroupName=group['logGroupName'])
            print(f"Deleted {group['logGroupName']}")

# Schedule via CloudWatch Events
lambda_handler(None, None)
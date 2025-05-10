import boto3
from datetime import datetime, timedelta

ce = boto3.client('ce')
end_date = datetime.utcnow().strftime('%Y-%m-%d')
start_date = (datetime.utcnow() - timedelta(days=30)).strftime('%Y-%m-%d')

response = ce.get_cost_forecast(
    TimePeriod={'Start': start_date, 'End': end_date},
    Metric='BLENDED_COST',
    Granularity='MONTHLY'
)
print(f"Forecasted monthly cost: ${response['Total']['Amount']}")
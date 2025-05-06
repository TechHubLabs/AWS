import boto3

def get_instance_pricing(instance_type, region='us-east-1'):
    pricing = boto3.client('pricing', region_name=region)
    response = pricing.get_products(
        ServiceCode='AmazonEC2',
        Filters=[
            {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type},
            {'Type': 'TERM_MATCH', 'Field': 'operatingSystem', 'Value': 'Linux'},
            {'Type': 'TERM_MATCH', 'Field': 'termType', 'Value': 'OnDemand'}
        ]
    )
    return response['PriceList']

# Example: Compare t3.micro On-Demand vs. 1-Year Reserved
print(get_instance_pricing('t3.micro'))
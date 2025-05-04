#!/bin/bash
# AWS CLI commands for common cost optimization tasks

# List unattached EBS volumes
aws ec2 describe-volumes --filters Name=status,Values=available --query "Volumes[*].[VolumeId,Size,VolumeType]" --output table

# Check Trusted Advisor cost optimization checks
aws support describe-trusted-advisor-checks --language en --query "checks[?category=='cost_optimizing']" --output table

# Get S3 storage costs by bucket (last month)
aws ce get-cost-and-usage \
  --time-period Start=$(date -d "-1 month" +%Y-%m-01),End=$(date +%Y-%m-01) \
  --granularity MONTHLY \
  --metrics "BlendedCost" \
  --filter '{"Dimensions":{"Key":"SERVICE","Values":["Amazon Simple Storage Service"]}}'
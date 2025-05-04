#!/bin/bash
# Example AWS CLI Cost Explorer query for EC2/S3 daily costs
aws ce get-cost-and-usage \
  --time-period Start=2023-01-01,End=2023-01-31 \
  --granularity DAILY \
  --metrics "BlendedCost" \
  --filter '{
    "Dimensions": {
      "Key": "SERVICE",
      "Values": ["Amazon Elastic Compute Cloud - Compute", "Amazon Simple Storage Service"]
    }
  }'
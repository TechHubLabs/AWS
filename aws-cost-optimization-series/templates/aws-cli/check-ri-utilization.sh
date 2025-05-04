#!/bin/bash
# Check Reserved Instance utilization
aws ce get-reservation-utilization \
  --time-period Start=2023-01-01,End=2023-01-31 \
  --granularity MONTHLY \
  --metrics "UtilizationPercentage" \
  --filter '{"Dimensions":{"Key":"SERVICE","Values":["Amazon Elastic Compute Cloud - Compute"]}}'
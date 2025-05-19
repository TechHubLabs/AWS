def calculate_break_even(ondemand_hourly, ri_hourly, ri_upfront):
    monthly_savings = (ondemand_hourly - ri_hourly) * 730  # 730 hrs/month
    break_even_months = ri_upfront / monthly_savings
    return break_even_months

# Example: t3.large On-Demand ($0.0832) vs 1-Year RI ($0.0416 + $500 upfront)
print(calculate_break_even(0.0832, 0.0416, 500))  # ~16.4 months
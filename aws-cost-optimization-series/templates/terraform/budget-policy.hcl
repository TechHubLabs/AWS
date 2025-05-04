resource "aws_budgets_budget" "monthly_ec2" {
  name         = "monthly-ec2-budget"
  budget_type  = "COST"
  limit_amount = "500"
  limit_unit   = "USD"
  time_unit    = "MONTHLY"

  notification {
    comparison_operator       = "GREATER_THAN"
    threshold                 = 100
    notification_type         = "ACTUAL"
    subscriber_email_addresses = ["alerts@yourcompany.com"]
  }
}

resource "aws_organizations_policy" "scp" {
  name        = "restrict-large-instances"
  description = "Block large instance types in dev accounts"
  content     = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Deny",
        Action   = "ec2:RunInstances",
        Resource = "*",
        Condition = {
          StringNotEqualsIfExists = {
            "ec2:InstanceType" = ["t3.micro", "t3.small"]
          }
        }
      }
    ]
  })
}
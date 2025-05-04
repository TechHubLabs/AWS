resource "aws_ce_cost_category" "team_allocation" {
  name = "team-cost-allocation"
  rule {
    value = "engineering"
    rule {
      dimensions {
        key = "TAG"
        values = ["team=engineering"]
      }
    }
  }
  rule {
    value = "marketing"
    rule {
      dimensions {
        key = "TAG"
        values = ["team=marketing"]
      }
    }
  }
}
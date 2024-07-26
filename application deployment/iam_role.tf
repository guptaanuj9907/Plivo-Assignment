provider "aws" {
  region = "ap-south-1"
}

# IAM Role for RDS Access
resource "aws_iam_role" "my_app_role" {
  name = "MyAppRDSAccessRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "eks.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

# IAM Policy for RDS Access
resource "aws_iam_policy" "my_app_rds_policy" {
  name        = "MyAppRDSAccessPolicy"
  description = "Policy to allow RDS access"
  policy      = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "rds:DescribeDBInstances",
          "rds:Connect"
        ],
        Resource = "*"
      }
    ]
  })
}

# Attach the policy to the role
resource "aws_iam_role_policy_attachment" "my_app_role_policy_attachment" {
  role       = aws_iam_role.my_app_role.name
  policy_arn  = aws_iam_policy.my_app_rds_policy.arn
}

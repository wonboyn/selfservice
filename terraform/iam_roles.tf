# ------------------
#
# Setup IAM Roles
#
# ------------------

###
# Role for Self Service Root Bot Lambda
###
resource "aws_iam_role" "root_bot_lambda_role" {
  name = "SelfService_Root_Bot_Lambda_Role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": [
          "lambda.amazonaws.com"
        ]
      }
    }
  ]
}
EOF
  tags = var.aws_resource_tags
}

# ------------------
#
# Setup IAM Policies
#
# ------------------

##
# Policy granting read access to the Skills table
###
resource "aws_iam_policy" "dynamodb_skills_table_read_policy" {
  name        = "SelfService_SkillsTable_Read_Policy"
  description = "Policy granting read access to Skills Dynamo DB table"
  policy = <<EOF
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": [
                "dynamodb:DescribeTable",
                "dynamodb:GetItem",
                "dynamodb:Scan",
                "dynamodb:Query"
            ],
            "Resource": [
                "${aws_dynamodb_table.skills_table.arn}"
            ]
        }
    ]
  }
  EOF
}


##
# Policy granting create log group access
###
resource "aws_iam_policy" "cloudwatch_log_group_create_policy" {
  name        = "SelfService_LogGroup_Create_Policy"
  description = "Policy granting create access for CloudWatch Log Groups"
  policy = <<EOF
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup"
            ],
            "Resource": [
                "arn:aws:logs:${aws_region}:${aws_account_id}:*"
            ]
        }
    ]
  }
  EOF
}


##
# Policy granting update Root Bot Lambda CloudWatch log access
###
resource "aws_iam_policy" "cloudwatch_log_root_bot_lambda_modify_policy" {
  name        = "SelfService_Modify_RootBot_Log_Policy"
  description = "Policy granting modify access for Root Bot Lambda CloudWatch Logs"
  policy = <<EOF
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "${aws_cloudwatch_log_group.root_bot_lambda_logs.arn}"
            ]
        }
    ]
  }
  EOF
}

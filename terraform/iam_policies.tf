# ------------------
#
# Setup IAM Policies
#
# ------------------

###
# Policy granting read access to the Skills table
###
data "aws_iam_policy_document" "skills_read_policy_doc" {
  statement {
    actions = [
       "dynamodb:DescribeTable",
       "dynamodb:GetItem",
       "dynamodb:Scan",
       "dynamodb:Query"
    ]
    resources = [
        aws_dynamodb_table.skills_table.arn
    ]
  }
}

resource "aws_iam_policy" "dynamodb_skills_table_read_policy" {
  name        = "SelfService_SkillsTable_Read_Policy"
  description = "Policy granting read access to Skills Dynamo DB table"
  policy      = data.aws_iam_policy_document.skills_read_policy_doc.json
}


###
# Policy granting create log group access
###
data "aws_iam_policy_document" "create_loggroup_policy_doc" {
  statement {
    actions = [
       "logs:CreateLogGroup"
    ]
    resources = [
        "arn:aws:logs:${var.aws_region}:${var.aws_account_id}:*"
    ]
  }
}

resource "aws_iam_policy" "cloudwatch_log_group_create_policy" {
  name        = "SelfService_LogGroup_Create_Policy"
  description = "Policy granting create access for CloudWatch Log Groups"
  policy      = data.aws_iam_policy_document.skills_read_policy_doc.json
}


###
# Policy granting update Root Bot Lambda CloudWatch log access
###
data "aws_iam_policy_document" "modify_root_bot_lambda_log_policy_doc" {
  statement {
    actions = [
       "logs:CreateLogStream",
       "logs:PutLogEvents"
    ]
    resources = [
        aws_cloudwatch_log_group.root_bot_lambda_logs.arn
    ]
  }
}

resource "aws_iam_policy" "cloudwatch_log_root_bot_lambda_modify_policy" {
  name        = "SelfService_Modify_RootBot_Log_Policy"
  description = "Policy granting modify access for Root Bot Lambda CloudWatch Logs"
  policy      = data.aws_iam_policy_document.modify_root_bot_lambda_log_policy_doc.json
}

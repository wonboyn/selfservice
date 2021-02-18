# -------------------------------------
#
# Setup attachment of policies to roles
#
# -------------------------------------

###
# Self Service API Gateway role policy attachment
###
resource "aws_iam_role_policy_attachment" "self_service_api_gateway_role_policy1" {
  role       = aws_iam_role.self_service_api_gateway_role.name
  policy_arn = aws_iam_policy.cloudwatch_log_group_create_policy.arn
}

resource "aws_iam_role_policy_attachment" "self_service_api_gateway_role_policy2" {
  role       = aws_iam_role.self_service_api_gateway_role.name
  policy_arn = aws_iam_policy.cloudwatch_log_self_service_api_gateway_modify_policy.arn
}


###
# Root Bot Lambda role policy attachment
###
resource "aws_iam_role_policy_attachment" "root_bot_lambda_role_policy1" {
  role       = aws_iam_role.root_bot_lambda_role.name
  policy_arn = aws_iam_policy.cloudwatch_log_group_create_policy.arn
}

resource "aws_iam_role_policy_attachment" "root_bot_lambda_role_policy2" {
  role       = aws_iam_role.root_bot_lambda_role.name
  policy_arn = aws_iam_policy.cloudwatch_log_root_bot_lambda_modify_policy.arn
}

resource "aws_iam_role_policy_attachment" "root_bot_lambda_role_policy3" {
  role       = aws_iam_role.root_bot_lambda_role.name
  policy_arn = aws_iam_policy.dynamodb_skills_table_read_policy.arn
}

# ----------------------
#
# AWS Terraform Outputs
#
# ----------------------

###
# API Gateway
###
output "api_gateway_definition_name" {
  description = "Name of the Self Service API Gateway"
  value       = aws_api_gateway_rest_api.self_service_api_gateway.name
}

output "api_gateway_definition_arn" {
  description = "ARN of the Self Service API Gateway"
  value       = aws_api_gateway_rest_api.self_service_api_gateway.arn
}

output "api_gateway_stage_url" {
  description = "URL of the Self Service API Gateway Stage Deployment"
  value       = aws_api_gateway_stage.self_service_api_gateway_stage.invoke_url
}


###
# CloudWatch Log Groups
###
output "cloudwatch_name_api_gateway" {
  description = "Name of the Self Service API Gateway CloudWatch Log Group"
  value       = aws_cloudwatch_log_group.self_service_api_gateway_cloudwatch_log_group.name
}

output "cloudwatch_arn_api_gateway" {
  description = "ARN of the Self Service API Gateway CloudWatch Log Group"
  value       = aws_cloudwatch_log_group.self_service_api_gateway_cloudwatch_log_group.arn
}

output "cloudwatch_name_root_bot_lambda" {
  description = "Name of the Self Service Root Bot Lambda CloudWatch Log Group"
  value       = aws_cloudwatch_log_group.root_bot_lambda_cloudwatch_log_group.name
}

output "cloudwatch_arn_root_bot_lambda" {
  description = "ARN of the Self Service Root Bot Lambda CloudWatch Log Group"
  value       = aws_cloudwatch_log_group.root_bot_lambda_cloudwatch_log_group.arn
}


###
# Dynamo DB
###
output "dynamodb_table_name_skills" {
  description = "Name of the Self Service Dynamo DB skills table name"
  value       = aws_dynamodb_table.skills_table.name
}

output "dynamodb_table_arn_skills" {
  description = "ARN of the Self Service Dynamo DB skills table name"
  value       = aws_dynamodb_table.skills_table.arn
}


###
# IAM Policies
###
output "policy_name_cloudwatch_log_group_create_permission" {
  description = "Name of the policy granting create permissions for CloudWatch log groups"
  value       = aws_iam_policy.cloudwatch_log_group_create_policy.name
}

output "policy_arn_cloudwatch_log_group_create_permission" {
  description = "ARN of the policy granting read permissions for CloudWatch log groups"
  value       = aws_iam_policy.cloudwatch_log_group_create_policy.arn
}

output "policy_name_api_gway_cloudwatch_log_modify_permission" {
  description = "Name of the policy granting modify permissions for CloudWatch logs for API Gateway"
  value       = aws_iam_policy.cloudwatch_log_self_service_api_gateway_modify_policy.name
}

output "policy_arn_api_gway_cloudwatch_log_modify_permission" {
  description = "ARN of the policy granting read permissions for CloudWatch logs for API Gateway"
  value       = aws_iam_policy.cloudwatch_log_self_service_api_gateway_modify_policy.arn
}

output "policy_name_rootbot_lambda_cloudwatch_log_modify_permission" {
  description = "Name of the policy granting modify permissions for CloudWatch logs for Root Bot Lambda"
  value       = aws_iam_policy.cloudwatch_log_root_bot_lambda_modify_policy.name
}

output "policy_arn_rootbot_lambda_cloudwatch_log_modify_permission" {
  description = "ARN of the policy granting read permissions for CloudWatch logs for Root Bot Lambda"
  value       = aws_iam_policy.cloudwatch_log_root_bot_lambda_modify_policy.arn
}

output "policy_name_dynamodb_skills_table_read_permission" {
  description = "Name of the policy granting read permissions for the Dynamo DB skills table"
  value       = aws_iam_policy.dynamodb_skills_table_read_policy.name
}

output "policy_arn_dynamodb_skills_table_read_permission" {
  description = "ARN of the policy granting read permissions for the Dynamo DB skills table"
  value       = aws_iam_policy.dynamodb_skills_table_read_policy.arn
}


###
# IAM Roles
###
output "role_name_api_gateway" {
  description = "Name of the role for Self Service API Gateway"
  value       = aws_iam_role.self_service_api_gateway_role.name
}

output "role_arn_api_gateway" {
  description = "ARN of the role for Self Service API Gateway"
  value       = aws_iam_role.self_service_api_gateway_role.arn
}

output "role_name_root_bot_lambda" {
  description = "Name of the role for Self Service Root Bot Lambda"
  value       = aws_iam_role.root_bot_lambda_role.name
}

output "role_arn_root_bot_lambda" {
  description = "ARN of the role for Self Service Root Bot Lambda"
  value       = aws_iam_role.root_bot_lambda_role.arn
}


###
# Lambda
###
output "lambda_name_root_bot" {
  description = "Name of the Self Service Dynamo DB skills table name"
  value       = aws_lambda_function.root_bot_lambda_function.function_name
}

output "lambda_arn_root_bot" {
  description = "ARN of the Self Service Dynamo DB skills table name"
  value       = aws_lambda_function.root_bot_lambda_function.arn
}


###
# S3 Bucket
###
output "s3_bucket_name_lambda_source" {
  description = "Name of the S3 Bucket used for Lambda source code"
  value       = aws_s3_bucket.s3_bucket_lambda_source.bucket
}

output "s3_bucket_arn_lambda_source" {
  description = "ARN of the S3 Bucket used for Lambda source code"
  value       = aws_s3_bucket.s3_bucket_lambda_source.arn
}

# ---------------------
#
# Terraform Variables
#
# ---------------------

###
# AWS general variables
###
variable "aws_account_id" {
  description = "AWS Account ID"
  type        = string
}

variable "aws_environment" {
  description = "AWS environment/stage [DEV/TEST/PROD]"
  type        = string
}

variable "aws_region" {
  description = "AWS Region"
  type        = string
}

variable "aws_resource_tags" {
  description = "Common Resource Tags"
  type        = map(string)
}


###
# API gateway variables
###
variable "api_gateway_selfservice_name" {
  description = "Name of the Self Service API Gateway REST endpoint"
  type        = string
}

variable "api_gateway_selfservice_desc" {
  description = "The description for the Self Service API Gateway REST endpoint"
  type        = string
}


###
# Dynamo DB variables
###
variable "dynamodb_skills_table_name" {
  description = "Name of the skills table in Dynamo DB"
  type        = string
}

variable "dynamodb_skills_table_tags" {
  description = "Tags to apply to the skills table"
  type        = map(string)
  default     = {}
}


###
# Root bot variables
###
variable "root_bot_cloudwatch_log_retention" {
  description = "The retention period for the lambda function logs"
  type        = number
}

variable "root_bot_lambda_function_desc" {
  description = "The description for the lambda function"
  type        = string
}

variable "root_bot_lambda_function_handler" {
  description = "The service handler path for the lambda function"
  type        = string
}

variable "root_bot_lambda_function_memory" {
  description = "The memory limit for the lambda function"
  type        = number
}

variable "root_bot_lambda_function_name" {
  description = "The name for the lambda function"
  type        = string
}

variable "root_bot_lambda_function_runtime" {
  description = "The runtime type for the lambda function"
  type        = string
  default     = "dotnetcore3.1"
}

variable "root_bot_lambda_function_tags" {
  description = "Tags to apply to the lambda function"
  type        = map(string)
  default     = {}
}

variable "root_bot_lambda_function_timeout" {
  description = "The timeout for the lambda function"
  type        = number
}

variable "root_bot_lambda_function_vars" {
  description = "Environment variables to apply to the lambda function"
  type        = map(string)
  default     = {}
}

variable "root_bot_lambda_source_s3_bucket_name" {
  description = "The name of the S3 bucket that has the root bot source zip"
  type        = string
}

variable "root_bot_lambda_source_s3_key" {
  description = "The name of the S3 bucket key that has the root bot source zip"
  type        = string
}

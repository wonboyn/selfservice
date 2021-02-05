# ---------------------
#
# Setup Lambdas
#
# ---------------------

##
# Root Bot Lambda definition
###
resource "aws_lambda_function" "root_bot_lambda_function" {
   function_name    = var.root_bot_lambda_function_name
   description      = var.root_bot_lambda_function_desc
   role             = var.root_bot_lambda_function_role
   handler          = var.root_bot_lambda_function_handler
   runtime          = var.root_bot_lambda_function_runtime
   memory_size      = var.root_bot_lambda_function_memory
   timeout          = var.root_bot_lambda_function_timeout
   tags             = merge(var.aws_resource_tags, var.root_bot_lambda_function_tags)
   s3_bucket        = var.root_bot_lambda_source_s3_bucket_name
   s3_key           = var.root_bot_lambda_source_s3_key

   dynamic "environment" {
      for_each = length(keys(var.root_bot_lambda_function_vars)) == 0 ? [] : [true]
      content {
         variables = var.root_bot_lambda_function_vars
      }
   }
}


###
# Root Bot Cloudwatch logs definition
###
resource "aws_cloudwatch_log_group" "lambda_service_logs" {
   name              = "/aws/lambda/${aws_lambda_function.root_bot_lambda_function.function_name}"
   retention_in_days = var.root_bot_cloudwatch_log_retention
}

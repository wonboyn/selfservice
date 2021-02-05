# -----------------------
#
# Default variable values
#
# -----------------------

###
# AWS variables
###
aws_region = "ap-southeast-2"
aws_resource_tags = {
    "application"   = "self-service"
    "environment"   = "DEV"
    "owner"         = "wonboyn@gmail.com"
    "provisioner"   = "terraform"
}


###
# Root bot variables
###
root_bot_cloudwatch_log_retention = "14"
root_bot_lambda_function_desc = "Self Service Root Bot"
root_bot_lambda_function_handler = "SelfService::RootBot.LambdaEntryPoint::FunctionHandlerAsync"
root_bot_lambda_function_memory = "128"
root_bot_lambda_function_name = "SelfServiceRootBot"
root_bot_lambda_function_timeout = "30"
root_bot_lambda_source_s3_bucket_name = ""
root_bot_lambda_source_s3_key = ""


###
# Dynamo DB variables
###
dynamodb_skills_table_name = "skills"

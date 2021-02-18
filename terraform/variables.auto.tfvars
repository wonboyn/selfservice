# -----------------------
#
# Default variable values
#
# -----------------------

###
# AWS general variables
###
aws_environment     = "DEV"
aws_region          = "ap-southeast-2"
aws_resource_tags   = {
    "application" = "self-service"
    "owner"       = "wonboyn@gmail.com"
    "provisioner" = "terraform"
}


###
# API gateway variables
###
api_gateway_selfservice_cloudwatch_log_retention = "14"
api_gateway_selfservice_endpoint_type            = "REGIONAL"
api_gateway_selfservice_name                     = "SelfService"
api_gateway_selfservice_desc                     = "Slack Self Service API"


###
# Dynamo DB variables
###
dynamodb_skills_table_name = "skills"


###
# Root bot variables
###
root_bot_cloudwatch_log_retention     = "14"
root_bot_lambda_function_desc         = "Self Service Root Bot"
root_bot_lambda_function_handler      = "SelfService::RootBot.LambdaEntryPoint::FunctionHandlerAsync"
root_bot_lambda_function_memory       = "128"
root_bot_lambda_function_name         = "SelfServiceRootBot"
root_bot_lambda_function_timeout      = "30"
root_bot_lambda_source_s3_bucket_name = "fred123lambdas"
root_bot_lambda_source_s3_key         = "rootbot/rootbot.zip"

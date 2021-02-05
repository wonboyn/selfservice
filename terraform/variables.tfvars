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
root_bot_cloudwatch_log_retention = ""
root_bot_lambda_function_desc = "Self Service Bot"
root_bot_lambda_function_handler = ""
root_bot_lambda_function_memory = "128"
root_bot_lambda_function_name = "Self Service Root Bot"
root_bot_lambda_function_role = ""
root_bot_lambda_function_runtime = "dotnetcore3.1"
root_bot_lambda_function_timeout = "30"
root_bot_lambda_source_s3_bucket_name = ""
root_bot_lambda_source_s3_key = ""


###
# Dynamo DB variables
###
dynamodb_skills_table_name = "skills"

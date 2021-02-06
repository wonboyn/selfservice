# ----------------------
#
# Setup API Gateway
#
# ----------------------

###
# Swagger definition for API Gateway
###
data "template_file" api_swagger {
  template = file("./self-service-swagger.yaml")
  vars     = {
    ProcessRootBotMessage = aws_lambda_function.root_bot_lambda_function.invoke_arn
  }
}


###
# API Gateway Definition
###
resource "aws_api_gateway_rest_api" "api_gateway" {
  name        = var.api_gateway_selfservice_name
  description = var.api_gateway_selfservice_desc
  body        = data.template_file.api_swagger.rendered
}


###
# API Gateway CloudWatch ARN
###
resource "aws_api_gateway_account" "api_gw_account" {
  cloudwatch_role_arn = aws_iam_role.cloudwatch.arn
}


###
# API Gateway Deployment
###
resource "aws_api_gateway_deployment" "api_gateway_deployment" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  stage_name  = var.aws_environment
}

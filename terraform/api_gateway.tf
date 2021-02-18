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
resource "aws_api_gateway_rest_api" "self_service_api_gateway" {
  name          = var.api_gateway_selfservice_name
  description   = var.api_gateway_selfservice_desc
  body          = data.template_file.api_swagger.rendered
  endpoint_configuration {
    types = [var.api_gateway_selfservice_endpoint_type] 
  }
}


###
# API Gateway CloudWatch logs definition
###
resource "aws_cloudwatch_log_group" "self_service_api_gateway_cloudwatch_log_group" {
   name              = "/aws/apigateway/${aws_api_gateway_rest_api.self_service_api_gateway.name}"
   retention_in_days = var.api_gateway_selfservice_cloudwatch_log_retention
   tags              = merge(
                        var.aws_resource_tags, 
                        var.api_gateway_selfservice_tags,
                        map("environment", var.aws_environment))
}


###
# API Gateway CloudWatch ARN
###
resource "aws_api_gateway_account" "self_service_api_gateway_account" {
  cloudwatch_role_arn = aws_iam_role.self_service_api_gateway_role.arn
}


###
# API Gateway Deployment
###
resource "aws_api_gateway_deployment" "self_service_api_gateway_deployment" {
  rest_api_id = aws_api_gateway_rest_api.self_service_api_gateway.id
  description = "Terraform deployment"
}


###
# API Gateway Stage
###
resource "aws_api_gateway_stage" "self_service_api_gateway_stage" {
  deployment_id = aws_api_gateway_deployment.self_service_api_gateway_deployment.id
  rest_api_id   = aws_api_gateway_rest_api.self_service_api_gateway.id
  stage_name    = var.aws_environment
}

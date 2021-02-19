# ------------------
#
# Setup IAM Roles
#
# ------------------

###
# Role for Self Service API Gateway REST Endpoint
###
resource "aws_iam_role" "self_service_api_gateway_role" {
   name = "SelfService_API_Gateway_Role"
   tags = var.aws_resource_tags
   assume_role_policy = <<EOF
{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "sts:AssumeRole",
         "Principal": {
           "Service": [
             "apigateway.amazonaws.com"
           ]
         }
       }
     ]
}
EOF
}


###
# Role for Self Service Root Bot Lambda
###
resource "aws_iam_role" "root_bot_lambda_role" {
   name = "SelfService_Root_Bot_Lambda_Role"
   tags = var.aws_resource_tags
   assume_role_policy = <<EOF
{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "sts:AssumeRole",
         "Principal": {
           "Service": [
             "lambda.amazonaws.com"
           ]
         }
       }
     ]
}
EOF
}

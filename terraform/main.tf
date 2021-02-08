# ---------------------
#
# Setup Terraform state
#
# ---------------------

#terraform {
#  backend "s3" {
#    bucket         = {{your_terraform_state_s3_bucket_name}}
#    key            = {{your_terraform_state_s3_key}}
#    region         = {{your_aws_region}}
#    dynamodb_table = {{your_terraform_state_dynamo_table_name}}
#    encrypt        = true
#  }
#}

#resource "aws_dynamodb_table" "terraform_self_service_locks" {
#  name         = {{your_terraform_state_dynamo_table_name}}
#  billing_mode = "PAY_PER_REQUEST"
#  hash_key     = "LockID"
#  attribute {
#    name = "LockID"
#    type = "S"
#  }
#}

terraform {
  backend "local" {
    path = "./terraform.tfstate"
  }
}

# --------------------
#
# AWS Terraform Config
#
# --------------------

###
# Setup Terraform config
###
terraform {

  # Minimum Terraform version
  required_version = ">= 0.14"

  # Required providers
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }

  # Terraform state
  backend "local" {
    path = "../tfstate/aws.tfstate"
  }
}


###
# Setup AWS provider
###
provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region     = var.aws_region
}

# -----------------------
#
# Azure Terraform Config
#
# -----------------------

###
# Setup Terraform config
###
terraform {

  # Minimum Terraform version
  required_version = ">= 0.14"

  # Required providers
  required_providers {
 
      # Hashicorp Random Provider
      random = {
         source = "hashicorp/random"
         version = "=3.1.0"
      }
      
      # Microsoft Azure Provider
      azurerm = {
         source = "hashicorp/azurerm"
         version = "=2.48.0"
      }

      # Microsoft Azure Active Directory Provider
      azuread = {
         source  = "hashicorp/azuread"
         version = "=1.4.0"
      }
  }


  # Terraform state
  backend "local" {
     path = "../tfstate/azure.tfstate"
  }
}


###
# Setup Azure provider
###
provider "azurerm" {
   features {}
}


###
# Import state from AWS phase
###
#data "terraform_remote_state" "aws_state" {
#  backend = "local" 
#  config = {
#    path    = "../tfstate/aws.tfstate"
#  }
#}

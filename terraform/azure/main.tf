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
      azurerm = {
      source = "hashicorp/azurerm"
      version = "=2.46.0"
    }
  }

  # Terraform state
  backend "local" {
    path = "../tfstate/aws.tfstate"
  }
}


###
# Setup Azure provider
###
provider "azurerm" {
  features {}
}

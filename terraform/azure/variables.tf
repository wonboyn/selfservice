# --------------------------
#
# Azure Terraform Variables
#
# --------------------------

###
# Azure general variables
###
variable "azure_client_id" {
   description = "Azure Client ID"
   type        = string
}

variable "azure_client_secret" {
   description = "Azure Client Secret"
   type        = string
}

variable "azure_environment" {
   description = "Azure environment/stage [DEV/TEST/PROD]"
   type        = string
}

variable "azure_location" {
   description = "Azure Location"
   type        = string
}

variable "azure_resource_tags" {
   description = "Common Resource Tags"
   type        = map(string)
}

variable "azure_tenant_id" {
   description = "Azure Tenant ID"
   type        = string
}


###
# Bot Registration
###
variable "bot_registration_resource_group_name" {
   description = "The name of the resource group for the Root Bot channel registration"
   type        = string
}

variable "bot_registration_name" {
   description = "The name for the Root Bot channel registration"
   type        = string
}

variable "bot_registration_sku" {
   description = "The SKU for the Root Bot channel registration"
   type        = string
}

variable "bot_registration_tags" {
   description = "Tags to apply to the Root Bot channel registration"
   type        = map(string)
   default     = {}
}

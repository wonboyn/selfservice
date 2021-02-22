# -------------------------------
#
# Setup Bot Services Registration
#
# -------------------------------

###
# Resource Group
###
resource "azurerm_resource_group" "root_bot_resource_group" {
   name     = var.bot_registration_resource_group_name
   location = var.azure_location
}


###
# Bot Service Registration
###
data "azurerm_client_config" "current" {}

resource "azurerm_bot_channels_registration" "root_bot_service_registration" {
   name                = var.bot_registration_name
   display_name        = var.bot_registration_name
#   endpoint            = data.terraform_remote_state.aws_state.output.api_gateway_stage_url
   location            = "global"
   resource_group_name = azurerm_resource_group.root_bot_resource_group.name
   sku                 = var.bot_registration_sku
   microsoft_app_id    = data.azurerm_client_config.current.client_id
   tags                = merge(
                          var.azure_resource_tags, 
                          var.bot_registration_tags,
                          map("environment", var.azure_environment))
}

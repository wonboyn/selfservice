# -------------------------------
#
# Setup Application Registration
#
# -------------------------------

###
# Resource Group
###
resource "azurerm_resource_group" "app_registration_resource_group" {
   name     = var.app_registration_resource_group_name
   location = var.azure_location
}


###
# App Registration
###
resource "azuread_application" "root_bot_app_registration" {
   display_name               = var.app_registration_name
   available_to_other_tenants = false
   oauth2_allow_implicit_flow = false
}

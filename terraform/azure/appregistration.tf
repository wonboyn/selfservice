# -------------------------------
#
# Setup Application Registration
#
# -------------------------------

###
# Generate Password
###
resource "random_password" "new_app_password" {
   length  = 32
   special = true
}


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


###
# App Registration Password
###
resource "azuread_application_password" "root_bot_app_password" {
   application_object_id = azuread_application.root_bot_app_registration.object_id
   value                 = random_password.new_app_password.result
   end_date_relative     = "17520h" # 2 years
}

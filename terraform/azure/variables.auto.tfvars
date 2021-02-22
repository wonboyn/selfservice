# ------------------------------
#
# Default Azure variable values
#
# ------------------------------

###
# Azure general variables
###
azure_environment   = "DEV"
azure_location      = "Australia East"
azure_resource_tags = {
    "application" = "self-service"
    "owner"       = "wonboyn@gmail.com"
    "provisioner" = "terraform"
}


###
# App Registration variables
###
app_registration_resource_group_name = "SelfService"
app_registration_name = "Fred"


###
# Bot Registration variables
###
bot_registration_resource_group_name = "SelfService"
bot_registration_name                = "SelfServiceRootBot"
bot_registration_sku                 = "F0"

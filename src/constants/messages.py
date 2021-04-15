###########################################################
# This module is used to centralise messages
# used by the self service bot.
#
###########################################################

class ErrorMessages:

    BOT_ABORT_ERROR = "Aborting Self Service Bot"
    BOT_INIT_ERROR = "ERROR reported during initialisation of SelfServiceBot"
    DYNAMODB_SCAN_ERROR = "ERROR reported by DynamoDB"
    GENERAL_ERROR = "The bot encountered an error."
    MISSING_PARAM_ERROR = "Required parameter not provided"
    MISSING_SKILLS_OBJ_ERROR = "Sills object not provided"

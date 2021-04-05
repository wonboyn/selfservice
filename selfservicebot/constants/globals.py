###########################################################
# This module is used to centralise constant values
# used by the self service bot.
#
###########################################################

class AwsApiGateway:

    KEY_MSG_BODY = "body"
    KEY_MSG_HEADERS = "headers"
    KEY_MSG_IS_BASE64 = "isBase64Encoded"
    KEY_MSG_STATUS_CODE = "statusCode"


class AwsLambda:

    KEY_EVENT_BODY = "body"
    KEY_EVENT_HEADERS = "headers"


class HttpHeaders:

    KEY_AUTHORIZATION = "Authorization"
    KEY_CONTENT_TYPE = "Content-Type"
    VAL_APPLICATION_JSON = "application/json"


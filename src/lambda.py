###########################################################
# This module provides the lambda entrypoint.
# 
###########################################################

# Third party imports
import asyncio
from http import HTTPStatus
import json

# Local imports
from common import processMsg
from constants import AwsApiGateway, AwsLambda, HttpHeaders



# Lambda handler entrypoint
def handler(event, context):

    # Grab the headers
    headers = event[AwsLambda.KEY_EVENT_HEADERS]

    # Did we receive an auth header?
    if HttpHeaders.KEY_AUTHORIZATION in headers:
        auth_header = headers[HttpHeaders.KEY_AUTHORIZATION]
    else:
        auth_header = ""

    # Grab the body
    bodyStr = event[AwsLambda.KEY_EVENT_BODY]
    body = json.loads(bodyStr)

    # Process the request in an async co-routine
    resp = asyncio.run(processMsg(auth_header, body))

    # Construct response for API Gateway
    hdrs = { HttpHeaders.KEY_CONTENT_TYPE: HttpHeaders.VAL_APPLICATION_JSON }
    response = dict()
    response.update({AwsApiGateway.KEY_MSG_IS_BASE64: False})
    response.update({AwsApiGateway.KEY_MSG_HEADERS: hdrs})
    
    if resp:
        response.update({AwsApiGateway.KEY_MSG_STATUS_CODE: str(resp.status)})
        response.update({AwsApiGateway.KEY_MSG_BODY: json.dumps(resp.body)})

    else:
        response.update({AwsApiGateway.KEY_MSG_STATUS_CODE: HTTPStatus.OK})
        response.update({AwsApiGateway.KEY_MSG_BODY: ""})

    # Send response
    return response

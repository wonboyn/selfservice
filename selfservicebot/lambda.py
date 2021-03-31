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


# # Separate async function to workaround
# # AWS Lambda limitation.
# async def main(auth_header, body):

#     # Process the message
#     response = await processMsg(auth_header, body)

#     # Build response object
#     hdrs = { "Content-Type": "application/json" }
#     resp = dict()
#     resp.update({"isBase64Encoded": False})
#     resp.update({"headers": hdrs})
    
#     if response:
#         resp.update({"statusCode": str(response.status)})
#         resp.update({"body": json.dumps(response.body)})

#     else:
#         resp.update({"statusCode": HTTPStatus.OK})
#         resp.update({"body": ""})

#     # Send response
#     return resp



# Lambda handler entrypoint
def handler(event, context):

    # Grab the headers
    headers = event["headers"]
    if "Authorization" in headers:
        auth_header = headers["Authorization"]
    else:
        auth_header = ""

    # Grab the body
    bodyStr = event["body"]
    body = json.loads(bodyStr)

    # Process the request in an async co-routine
    #response = asyncio.run(main(auth_header, body))
    resp = asyncio.run(processMsg(auth_header, body))

    # Construct response for API Gateway
    hdrs = { "Content-Type": "application/json" }
    response = dict()
    response.update({"isBase64Encoded": False})
    response.update({"headers": hdrs})
    
    if resp:
        response.update({"statusCode": str(resp.status)})
        response.update({"body": json.dumps(resp.body)})

    else:
        response.update({"statusCode": HTTPStatus.OK})
        response.update({"body": ""})

    # Send response
    return response

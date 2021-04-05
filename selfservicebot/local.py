###########################################################
# This module is used for local testing of the 
# self service bot using the Bot Framework emulator.
# It runs a local web server & processes any requests
# received on the /api/messages endpoint.
###########################################################

# Third party imports
from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core.integration import aiohttp_error_middleware
from http import HTTPStatus

# Local imports
from common import processMsg
from constants import HttpHeaders

# Web server binding constants
HOST = "localhost"
PORT = 3978
ROUTE = "/api/messages"



# Setup handler for inbound bot requests
async def messages(req: Request) -> Response:

    # Ensure request is json based
    if HttpHeaders.VAL_APPLICATION_JSON in req.headers[HttpHeaders.KEY_CONTENT_TYPE]:
        body = await req.json()
    else:
        return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

    # Extract the auth headers if available
    if HttpHeaders.KEY_AUTHORIZATION in req.headers:
        auth_header = req.headers[HttpHeaders.KEY_AUTHORIZATION]
    else:
        auth_header = ""

    # Process the message
    response = await processMsg(auth_header, body)

    # Build response object
    if response:
        return json_response(data=response.body, status=response.status)

    else:
        return Response(status=HTTPStatus.OK)



# Listen for incoming requests on /api/messages
APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post(ROUTE, messages)

if __name__ == "__main__":
    try:
        web.run_app(APP, host=HOST, port=PORT)
    except Exception as error:
        raise error

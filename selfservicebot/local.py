###########################################################
# This module is used for local testing of the 
# self service bot using the Bot emulator. It 
# runs a local web server & processes any requests
# received on the /api/messages endpoint.
###########################################################

# Third party imports
from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core.integration import aiohttp_error_middleware
from http import HTTPStatus

# Local imports
from common import processMsg

# Port that the web server should listen on
PORT = 3978


# Setup handler for inbound bot requests
async def messages(req: Request) -> Response:
    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
    else:
        return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    # Process the message
    response = await processMsg(auth_header, body)

    # Build response object
    if response:
        return json_response(data=response.body, status=response.status)

    else:
        return Response(status=HTTPStatus.OK)



# Listen for incoming requests on /api/messages
APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    try:
        web.run_app(APP, host="localhost", port=PORT)
    except Exception as error:
        raise error

###########################################################
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
###########################################################

from http import HTTPStatus

from aiohttp import web
from aiohttp.web import Request, Response
from aiohttp.web_response import json_response
from botbuilder.core import BotFrameworkAdapterSettings, ConversationState, MemoryStorage
from botbuilder.core.integration import aiohttp_channel_service_routes, aiohttp_error_middleware
from botbuilder.core.skills import SkillHandler
from botbuilder.integration.aiohttp.skills import SkillHttpClient
from botbuilder.schema import Activity
from botframework.connector.auth import AuthenticationConfiguration, SimpleCredentialProvider

from adapters import AdapterWithErrorHandler, SkillConversationIdFactory
from authentication import AllowedSkillsClaimsValidator
from bots import MainBot
from config import BotConfig, SkillConfiguration

# Load the configuration
CONFIG = BotConfig()
SKILL_CONFIG = SkillConfiguration()

# Whitelist skills from SKILL_CONFIG
AUTH_CONFIG = AuthenticationConfiguration(
    claims_validator=AllowedSkillsClaimsValidator(CONFIG).claims_validator
)

# Setup the Bot settings
SETTINGS = BotFrameworkAdapterSettings(
    app_id=CONFIG.APP_ID,
    app_password=CONFIG.APP_PASSWORD,
    auth_configuration=AUTH_CONFIG,
)
STORAGE = MemoryStorage()
CONVERSATION_STATE = ConversationState(STORAGE)
ID_FACTORY = SkillConversationIdFactory(STORAGE)
CREDENTIAL_PROVIDER = SimpleCredentialProvider(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
CLIENT = SkillHttpClient(CREDENTIAL_PROVIDER, ID_FACTORY)

# Create adapter.
ADAPTER = AdapterWithErrorHandler(
    SETTINGS, CONFIG, CONVERSATION_STATE, CLIENT, SKILL_CONFIG
)

# Create the Self Service Bot
BOT = MainBot(CONVERSATION_STATE, SKILL_CONFIG, CLIENT, CONFIG)

# Create the handler for processing skills
SKILL_HANDLER = SkillHandler(
    ADAPTER, BOT, ID_FACTORY, CREDENTIAL_PROVIDER, AUTH_CONFIG
)

# Setup handler for inbound bot requests
async def messages(req: Request) -> Response:
    # Main bot message handler.
    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
    else:
        return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

    activity = Activity().deserialize(body)
    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    invoke_response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if invoke_response:
        return json_response(data=invoke_response.body, status=invoke_response.status)
    return Response(status=HTTPStatus.OK)

# Listen for incoming requests on /api/messages
APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/messages", messages)
APP.router.add_routes(aiohttp_channel_service_routes(SKILL_HANDLER, "/api/skills"))

if __name__ == "__main__":
    try:
        web.run_app(APP, host="localhost", port=CONFIG.PORT)
    except Exception as error:
        raise error
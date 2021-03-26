# DEBUG
import sys
print (sys.path)

# Third party imports
from botbuilder.core import BotFrameworkAdapterSettings, ConversationState, MemoryStorage
from botbuilder.core.skills import SkillHandler
from botbuilder.integration.aiohttp.skills import SkillHttpClient
from botbuilder.schema import Activity
from botframework.connector.auth import AuthenticationConfiguration, SimpleCredentialProvider
from http import HTTPStatus

# Local imports
from adapters import AdapterWithErrorHandler, SkillConversationIdFactory
from authentication import AllowedSkillsClaimsValidator
from bots import MainBot
from config import BotConfig, SkillConfiguration
import asyncio, json


# Async main function
async def main(auth_header, body):

    # Load the bot configuration
    CONFIG = BotConfig()

    # Load the skill configuration
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

    # Grab the message activity
    activity = Activity().deserialize(body)

    # Call bot
    invoke_response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)

    # Handle error response
    if invoke_response:
        return {
            "statusCode": str(invoke_response.status),
            "body": json.dumps(invoke_response.body),
            "headers": {
                "Content-Type": "application/json"
            },
        }
    
    # Handle successful response
    return { "statusCode": str(HTTPStatus.OK) }



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

    # Call the async main function
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main(auth_header, body))

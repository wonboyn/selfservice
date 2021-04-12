###########################################################
# This module contains the main logic for
# configuring & running the Bot Framework.
# 
###########################################################

# Third party imports
from botbuilder.core import BotFrameworkAdapterSettings, TurnContext, BotFrameworkAdapter
from botbuilder.schema import Activity, ActivityTypes
import sys
import traceback

# Local imports
from bots import SelfServiceBot
from cards import ErrorCard
from config import BotConfig
from constants import ErrorMessages


# Load the bot configuration
CONFIG = BotConfig()


# Configure the Bot settings
SETTINGS = BotFrameworkAdapterSettings(
    app_id=CONFIG.APP_ID,
    app_password=CONFIG.APP_PASSWORD
)


# Create adapter.
ADAPTER = BotFrameworkAdapter(SETTINGS)


# Define a Catch-all handler for errors.
async def on_error(context: TurnContext, error: Exception):

    # Log the exception
    print(f"ERROR: {error}", file=sys.stdout)
    traceback.print_exc(file=sys.stdout)

    # Send a message to the user
    card = ErrorCard(ErrorMessages.GENERAL_ERROR)
    message = await card.genMessage()
    await context.send_activity(message)
    

# Set the adapter to use the error handler
ADAPTER.on_turn_error = on_error


# Create the Self Service Bot
try: 
    BOT = SelfServiceBot()
except:
    print(ErrorMessages.BOT_ABORT_ERROR, file=sys.stdout)
    sys.exit(1)


# Setup handler for processing inbound bot requests
async def processMsg(auth_header, body):

    # Create activity
    activity = Activity().deserialize(body)

    # Call the bot
    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)

    # Return the response
    return response

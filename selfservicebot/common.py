###########################################################
# This module contains the main logic for
# configuring & running the Bot Framework.
# 
###########################################################

# Third party imports
from botbuilder.core import BotFrameworkAdapterSettings, TurnContext, BotFrameworkAdapter
from botbuilder.schema import Activity, ActivityTypes
from datetime import datetime
import sys
import traceback

# Local imports
from bots import SelfServiceBot
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

    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity(ErrorMessages.GENERAL_ERROR)
    
    # Send a trace activity if we're talking to the Bot Framework Emulator
    if context.activity.channel_id == "emulator":

        trace_activity = Activity(
            label="TurnError",
            name="on_turn_error Trace",
            timestamp=datetime.utcnow(),
            type=ActivityTypes.trace,
            value=f"{error}",
            value_type="https://www.botframework.com/schemas/error",
        )
        await context.send_activity(trace_activity)


# Set the adapter to use the error handler
ADAPTER.on_turn_error = on_error


# Create the Self Service Bot
BOT = SelfServiceBot()


# Setup handler for processing inbound bot requests
async def processMsg(auth_header, body):

    # Create activity
    activity = Activity().deserialize(body)

    # Call the bot
    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)

    # Return the response
    return response

# Third party imports
from botbuilder.core import BotFrameworkAdapterSettings, TurnContext, BotFrameworkAdapter
from botbuilder.schema import Activity, ActivityTypes
from datetime import datetime
import sys
import traceback

# Local imports
from bots import SelfServiceBot
from config import BotConfig
from skills import Skills


# Load the bot configuration
CONFIG = BotConfig()


# Load the available skills
SKILLS = Skills()


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
    await context.send_activity("The bot encountered an error or bug.")
    await context.send_activity(
        "To continue to run this bot, please fix the bot source code."
    )
    # Send a trace activity if we're talking to the Bot Framework Emulator
    if context.activity.channel_id == "emulator":
        # Create a trace activity that contains the error object
        trace_activity = Activity(
            label="TurnError",
            name="on_turn_error Trace",
            timestamp=datetime.utcnow(),
            type=ActivityTypes.trace,
            value=f"{error}",
            value_type="https://www.botframework.com/schemas/error",
        )
        # Send a trace activity, which will be displayed in Bot Framework Emulator
        await context.send_activity(trace_activity)


# Create the Self Service Bot
BOT = SelfServiceBot(SKILLS)


# Setup handler for processing inbound bot requests
async def processMsg(auth_header, body):

    # Create activity
    activity = Activity().deserialize(body)

    # Call the bot
    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)

    # Return the response
    return response

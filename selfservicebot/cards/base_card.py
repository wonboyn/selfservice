###########################################################
# This module provides a base template class for
# generating an adaptive card.
# 
###########################################################

# Third party imports
from adaptivecardbuilder import AdaptiveCard, TextBlock
from botbuilder.core import CardFactory
from botbuilder.schema import Activity, ActivityTypes
import json


class BaseCard():
    """The BaseCard class is used to represent a base adaptive card."""

    def __init__(self):

        self.card = AdaptiveCard()
        self.card.add(TextBlock("Self Service Bot", size="ExtraLarge", weight="Bolder"))


    async def genMessage(self) -> Activity:
        """Generate the Activity object containing the adapative card message."""

        # Generate the JSON object for the card
        cardJsonStr = await self.card.to_json()
        cardJson = json.loads(cardJsonStr)

        # Create the Adaptive Card message
        message = Activity(
                type = ActivityTypes.message,
                attachments = [CardFactory.adaptive_card(cardJson)]
        )

        # Return the message
        return message

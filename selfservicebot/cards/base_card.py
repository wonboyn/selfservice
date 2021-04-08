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

    def __init__(self):

        self.card = AdaptiveCard()
        self.card.add(TextBlock("Self Service Bot", size="ExtraLarge", weight="Bolder"))


    async def genMessage(self):

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

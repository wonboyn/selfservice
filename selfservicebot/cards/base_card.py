###########################################################
# This module provides a base template class for
# generating an adaptive card.
# 
###########################################################

# Third party imports
from adaptivecardbuilder import AdaptiveCard, TextBlock

# Local imports
import json


class BaseCard():

    def __init__(self):

        self.card = AdaptiveCard()
        self.card.add(TextBlock("Self Service Bot", size="ExtraLarge", weight="Bolder"))


    async def genCard(self):

        cardJsonStr = await self.card.to_json()
        cardJson = json.loads(cardJsonStr)
        return cardJson

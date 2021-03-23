# Third party imports
from adaptivecardbuilder import AdaptiveCard, Column, ColumnSet, TextBlock

# Local imports
import json


class WelcomeCard():

    def __init__(self):

        self.card = AdaptiveCard()
        self.card.add([
            TextBlock(text="Self Service Bot", size="ExtraLarge", weight="Bolder"),
            TextBlock(text="Welcome to the Self Service Bot. For a list of commands type \"help\".", size="Small")
        ])


    async def genCard(self):

        cardJsonStr = await self.card.to_json()
        cardJson = json.loads(cardJsonStr)
        return cardJson

from adaptivecardbuilder import AdaptiveCard, Column, ColumnSet, TextBlock

class WelcomeCard():

    def __init__(self):

        self.card = AdaptiveCard()
        self.card.add([
            TextBlock(text="Self Service Bot", size="ExtraLarge", weight="Bolder"),
            TextBlock(text="Welcome to the Self Service Bot. For a list of commands type \"help\".", size="Small"),
            #TextBlock(text="For a list of commands type \"help\"", size="Small"),
            TextBlock(text="For help with a specific command type \"help {command_name}\"", size="Small")
        ])


    async def genCard(self):

        return await self.card.to_json()

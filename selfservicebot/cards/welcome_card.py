from adaptivecardbuilder import AdaptiveCard, Column, ColumnSet, TextBlock

class WelcomeCard():

    def __init__(self):

        self.card = AdaptiveCard()
        self.card.add([
            TextBlock("Welcome to the Self Service Bot"),
            ColumnSet(),
                Column(),
                    TextBlock("Column 1 Top Item"),
                    TextBlock("Column 1 Second Item"),
                    "<",
                Column(),
                    TextBlock("Column 2 Top Item"),
                    TextBlock("Column 2 Second Item"),
                    "<",
                "<",
            TextBlock("Lowest Level")
        ])


    async def genCard(self):

        return await self.card.to_json()

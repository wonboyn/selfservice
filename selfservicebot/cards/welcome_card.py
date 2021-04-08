###########################################################
# This module provides a class for generating a basic
# welcome adaptive card. 
# 
###########################################################

# Third party imports
from adaptivecardbuilder import ActionSubmit, TextBlock

# Local imports
from cards.base_card import BaseCard


class WelcomeCard(BaseCard):

    def __init__(self):

        super().__init__()
        data = dict()
        data.update({"skill": "help"})
        self.card.add(TextBlock("Welcome to the Self Service Bot.", size="small"))
        self.card.add(TextBlock("For a list of skills click the button below.", size="small"))
        self.card.add(ActionSubmit(title="Get Help", data=data))

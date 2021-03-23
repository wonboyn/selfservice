# Third party imports
from adaptivecardbuilder import TextBlock

# Local imports
from cards.base_card import BaseCard


class WelcomeCard(BaseCard):

    def __init__(self):

        super().__init__()
        self.card.add(TextBlock("Welcome to the Self Service Bot.", size="small"))

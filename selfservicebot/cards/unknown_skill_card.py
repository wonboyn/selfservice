# Third party imports
from adaptivecardbuilder import AdaptiveCard, TextBlock

# Local imports
from cards.base_card import BaseCard


class UnknownSkillCard(BaseCard):

    def __init__(self, cmd):

        super().__init__()
        self.card.add(TextBlock("Unknown command: " + cmd, size="small"))
        self.card.add(TextBlock("For a list of available commands enter \"help\".", size="small"))

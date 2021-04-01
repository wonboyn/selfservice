# Third party imports
from adaptivecardbuilder import ActionSubmit, TextBlock

# Local imports
from cards.base_card import BaseCard


class UnknownSkillCard(BaseCard):

    def __init__(self, skill):

        super().__init__()
        self.card.add(TextBlock("Unknown skill: " + skill, size="small"))
        self.card.add(TextBlock("For a list of skills click the button below.", size="small"))
        self.card.add(ActionSubmit(title="Get Help", data={"skill":"help"}))

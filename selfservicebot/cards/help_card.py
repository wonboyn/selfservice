###########################################################
# This module provides a class for generating a basic
# help adaptive card. The card provides a list of the
# available skills.
# 
###########################################################

# Third party imports
from adaptivecardbuilder import Fact, FactSet, TextBlock

# Local imports
from cards.base_card import BaseCard


class HelpCard(BaseCard):

    def __init__(self, skills):

        super().__init__()
        self.card.add(TextBlock("The following skills are available.", size="small"))
        self.card.add(FactSet())
        for name in skills.keys():
            botskill = skills[name]
            self.card.add(Fact(name, botskill.description)) 

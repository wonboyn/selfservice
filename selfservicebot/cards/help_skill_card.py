###########################################################
# This module provides a class for generating a detailed
# help adaptive card. The card provides a details on a
# specific skill.
# 
###########################################################

# Third party imports
from adaptivecardbuilder import Fact, FactSet, TextBlock

# Local imports
from cards.base_card import BaseCard


class HelpSkillCard(BaseCard):

    def __init__(self, skill):

        super().__init__()
        self.card.add(TextBlock("The following skills are available.", size="small"))
        self.card.add(FactSet())
        # for name in skills.keys():
        #     botskill = skills[name]
        #     self.card.add(Fact(name, botskill.description)) 

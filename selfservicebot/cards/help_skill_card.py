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

        # Get skill details
        name = skill.getName()
        cat = skill.getCategory()
        desc = skill.getDesc()

        self.card.add(TextBlock("Skill details.", size="small"))
        self.card.add(FactSet())
        self.card.add(Fact("Name", name)) 
        self.card.add(Fact("Category", cat)) 
        self.card.add(Fact("Description", desc)) 

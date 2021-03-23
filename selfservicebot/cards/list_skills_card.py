# Third party imports
from adaptivecardbuilder import Fact, FactSet, TextBlock

# Local imports
from cards.base_card import BaseCard
from skills import BotSkill


class ListSkillsCard(BaseCard):

    def __init__(self, skills):

        super().__init__()
        self.card.add(TextBlock("The following commands are available.", size="small"))
        self.card.add(FactSet())
        for name in skills.keys():
            botskill = skills[name]
            self.card.add(Fact(name, botskill.description)) 

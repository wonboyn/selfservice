# Third party imports
from adaptivecardbuilder import AdaptiveCard, Fact, FactSet, TextBlock

# Local imports
import json
from skills import BotSkill


class ListSkillsCard():

    def __init__(self, skills_config):

        # Grab the list of skills
        skills = skills_config.SKILLS

        # Create Card
        self.card = AdaptiveCard()
        self.card.add(TextBlock("Self Service Bot Skills", size="ExtraLarge", weight="Bolder"))
        self.card.add(FactSet())
        for name in skills.keys():
            botskill = skills[name]
            self.card.add(Fact(name, botskill.description)) 


    async def genCard(self):

        cardJsonStr = await self.card.to_json()
        cardJson = json.loads(cardJsonStr)
        return cardJson

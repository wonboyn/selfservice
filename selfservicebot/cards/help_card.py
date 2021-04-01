###########################################################
# This module provides a class for generating a basic
# help adaptive card. The card provides a list of the
# available skills.
# 
###########################################################

# Third party imports
from adaptivecardbuilder import ActionSet, ActionSubmit, Column, ColumnSet, TextBlock

# Local imports
from cards.base_card import BaseCard


class HelpCard(BaseCard):

    def __init__(self, skills):

        super().__init__()
        self.card.add(TextBlock("The following skills are available.", size="small"))

        # Icon url for table
        #icon_url = "https://fontawesome.com/icons/info-circle?style=solid"

        # Iterate the skills
        for name in skills.keys():

            # Retrieve the skill
            botskill = skills[name]

            # Add Column for name
            self.card.add(ColumnSet())
            self.card.add(Column(width=1))
            self.card.add(TextBlock(text=name, horizontalAlignment="center"))
            self.card.up_one_level()

            # Add Column for description
            self.card.add(Column(width=2))
            self.card.add(TextBlock(text=botskill.description, horizontalAlignment="left"))
            self.card.up_one_level()

            # Add Column for button
            data = dict()
            data.update({"skill": "help"})
            data.update({"name": name})
            self.card.add(Column(width=1))
            self.card.add(ActionSet())
            #self.card.add(ActionSubmit(iconUrl=flag_url, data=data), is_action=True)
            self.card.add(ActionSubmit(title="Detail", data=data))
            self.card.back_to_top()

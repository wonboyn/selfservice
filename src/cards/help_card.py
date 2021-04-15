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
from constants import ErrorMessages


class HelpCard(BaseCard):
    """The HelpCard class is an extension of the BaseCard that is used for listing skills."""

    def __init__(self, skills):

        # Sanity check
        if not skills:
            raise Exception(ErrorMessages.MISSING_SKILLS_OBJ_ERROR)

        # Setup the card
        super().__init__()
        self.card.add(TextBlock("The following skills are available.", size="small"))

        # Iterate the skills
        for name in skills.keys():

            # Retrieve the skill details
            skill = skills[name]
            desc = skill.getDesc()

            # Create dictionary for info button
            info = dict()
            info.update({"skill": "help"})
            info.update({"name": name})

            # Create dictionary for run button
            run = dict()
            run.update({"skill": "name"})

            # Add Column for name
            self.card.add(ColumnSet())
            self.card.add(Column(width=1))
            self.card.add(TextBlock(text=name, horizontalAlignment="left"))
            self.card.up_one_level()

            # Add Column for description
            self.card.add(Column(width=2))
            self.card.add(TextBlock(text=desc, horizontalAlignment="left"))
            self.card.up_one_level()

            # Add Column for action buttons
            self.card.add(Column(width=1))
            self.card.add(ActionSet())
            self.card.add(ActionSubmit(title="Info", data=info))
            self.card.add(ActionSubmit(title="Run", data=run))
            self.card.back_to_top()

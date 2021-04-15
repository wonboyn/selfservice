###########################################################
# This module provides a class for generating a basic
# error adaptive card. The card provides a text block.
# 
###########################################################

# Third party imports
from adaptivecardbuilder import TextBlock

# Local imports
from cards.base_card import BaseCard


class ErrorCard(BaseCard):
    """The ErrorCard class is an extension of the BaseCard that is used for any error messages."""

    def __init__(self, message):

        super().__init__()
        self.card.add(TextBlock(message, size="small"))

###########################################################
# This module contains the logic for the Self 
# Service Bot itself.
# 
###########################################################

# Third party imports
from botbuilder.core import ActivityHandler, CardFactory, MessageFactory, TurnContext
from botbuilder.schema import Activity, ActivityTypes, ChannelAccount

# Local imports
from cards import ListSkillsCard, UnknownSkillCard, WelcomeCard
from skills import Skills
from typing import List



class SelfServiceBot(ActivityHandler):

    # Constructor
    def __init__(self):

        # Load skills
        skillsObj = Skills()
        self._skills = skillsObj.getSkills()


    # Handler for any members being added to the channel
    async def on_members_added_activity(
        self, members_added: List[ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:

                # Generate welcome card
                card = WelcomeCard()
                cardJson = await card.genCard()

                # Create message to send
                message = Activity(
                    type = ActivityTypes.message,
                    attachments = [CardFactory.adaptive_card(cardJson)]
                )

                # Send response
                await turn_context.send_activity(message)


    # Handler for any messages to the bot
    async def on_message_activity(self, turn_context: TurnContext):

        req = turn_context.activity.text.lower()

        # Call for help?
        if req.startswith("help"):

            # Generate skills list card
            card = ListSkillsCard(self._skills)
            cardJson = await card.genCard()

            # Create message to send
            message = Activity(
                type = ActivityTypes.message,
                attachments = [CardFactory.adaptive_card(cardJson)]
            )

            # Send response
            await turn_context.send_activity(message)


        # Call to run skill?
        elif req in self._skills:

            # Begin forwarding Activities to the skill
            await turn_context.send_activity(
                MessageFactory.text("Got it, connecting you to the skill...")
            )

            skill = "fred"
            # Save active skill in state
            await self._active_skill_property.set(turn_context, skill)

            # Send the activity to the skill
            await self.__send_to_skill(turn_context, skill)


        # No idea what to do!
        else:

            # Generate unknown skill card
            card = UnknownSkillCard(req)
            cardJson = await card.genCard()

            # Create message to send
            message = Activity(
                type = ActivityTypes.message,
                attachments = [CardFactory.adaptive_card(cardJson)]
            )

            # Send response
            await turn_context.send_activity(message)


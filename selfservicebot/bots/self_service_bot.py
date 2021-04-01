###########################################################
# This module contains the logic for the Self 
# Service Bot itself.
# 
###########################################################

# Third party imports
from botbuilder.core import ActivityHandler, CardFactory, MessageFactory, TurnContext
from botbuilder.schema import Activity, ActivityTypes, ChannelAccount

# Local imports
from cards import HelpCard, HelpSkillCard, UnknownSkillCard, WelcomeCard
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

        # Get the request
        if turn_context.activity.text is None:

            # No text provided so check the activity value
            if not bool(turn_context.activity.value):

                # No text & no value.
                # We should not end up here!
                return

            else:

                # Check for skill
                if "skill" in turn_context.activity.value:
                    req = turn_context.activity.value["skill"].lower()

        
        else:
            req = turn_context.activity.text.lower()


        # Call for help?
        if req.startswith("help"):

            # Basic or detailed help?
            args = req.split()
            if len(args) > 1:

                # Detailed help
                message = await self.__doHelpSkill(args[1])

            else:

                # Basic help
                message = await self.__doHelp()

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

            # Create message to send
            message = await self.__doUnknownSkill(req)

            # Send response
            await turn_context.send_activity(message)


    # Handle basic help request
    async def __doHelp(self):

        # Generate adaptive card
        card = HelpCard(self._skills)
        cardJson = await card.genCard()

        # Create message
        message = Activity(
                type = ActivityTypes.message,
                attachments = [CardFactory.adaptive_card(cardJson)]
        )

        # Return the message
        return message


    # Handle skill help request
    async def __doHelpSkill(self, arg):

        # Check that the skill exists
        if arg in self._skills:

            # Generate adaptive card
            skill = self._skills[arg]
            card = HelpSkillCard(skill)
            cardJson = await card.genCard()

        else:

            # Unknown skills requested
            card = UnknownSkillCard(arg)
            cardJson = await card.genCard()

        # Create message
        message = Activity(
                type = ActivityTypes.message,
                attachments = [CardFactory.adaptive_card(cardJson)]
        )

        # Return the message
        return message


    # Handle unknown skill
    async def __doUnknownSkill(self, skill):

        # Generate unknown skill card
        card = UnknownSkillCard(skill)
        cardJson = await card.genCard()

        # Create message
        message = Activity(
                type = ActivityTypes.message,
                attachments = [CardFactory.adaptive_card(cardJson)]
        )

        # Return the message
        return message

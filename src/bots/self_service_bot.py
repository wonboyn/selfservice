###########################################################
# This module contains the logic for the Self 
# Service Bot itself.
# 
###########################################################

# Third party imports
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
import sys

# Local imports
from botocore.exceptions import ClientError
from cards import HelpCard, HelpSkillCard, UnknownSkillCard, WelcomeCard
from constants import ErrorMessages
from skills import Skills
from typing import List



class SelfServiceBot(ActivityHandler):

    # Constructor
    def __init__(self):

        # Load skills
        try:
            skillsObj = Skills()
        except ClientError:
            print(ErrorMessages.BOT_INIT_ERROR, file=sys.stdout)
            raise

        # Set the skills member variable
        self._skills = skillsObj.getSkills()


    # Handler for any members being added to the channel
    async def on_members_added_activity(
        self, members_added: List[ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:

                # Generate welcome card
                card = WelcomeCard()
                message = await card.genMessage()

                # Send response
                await turn_context.send_activity(message)


    # Handler for any messages to the bot
    async def on_message_activity(self, turn_context: TurnContext):

        # Check the activity text
        req = dict()
        if turn_context.activity.text is None:

            # No text provided so check the activity value
            if not bool(turn_context.activity.value):

                # No text & no value.
                # We should not end up here!
                return

            else:

                # Check for skill
                if "skill" in turn_context.activity.value:

                    # Iterate the values 
                    for key in turn_context.activity.value.keys():
                        req.update({key: turn_context.activity.value[key].lower()})

                else:

                    # No skill provided
                    # We should not end up here!
                    return

        
        else:

            # Parse the activity text
            text = turn_context.activity.text.lower()
            args = text.split(" ", 1)
            req.update({"skill": args[0]})
            if len(args) > 1:
                req.update({"name": args[1]})


        # Call for help?
        if req["skill"] == "help":

            # Basic or detailed help?
            if "name" in req:

                # Detailed help
                message = await self.__doHelpSkill(req["name"])

            else:

                # Basic help
                message = await self.__doHelp()

            # Send response
            await turn_context.send_activity(message)


        # Call to run skill?
        elif req["skill"] in self._skills:

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
            message = await self.__doUnknownSkill(req["skill"])

            # Send response
            await turn_context.send_activity(message)


    # Handle basic help request
    async def __doHelp(self):

        # Generate adaptive card
        card = HelpCard(self._skills)
        message = await card.genMessage()

        # Return the message
        return message


    # Handle skill help request
    async def __doHelpSkill(self, arg):

        # Check that the skill exists
        if arg in self._skills:

            # Generate adaptive card
            skill = self._skills[arg]
            card = HelpSkillCard(skill)
            message = await card.genMessage()

        else:

            # Unknown skills requested
            card = UnknownSkillCard(arg)
            message = await card.genMessage()

        # Return the message
        return message


    # Handle unknown skill
    async def __doUnknownSkill(self, skill):

        # Generate unknown skill card
        card = UnknownSkillCard(skill)
        message = await card.genMessage()

        # Return the message
        return message

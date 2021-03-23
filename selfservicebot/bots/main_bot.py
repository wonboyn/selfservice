###########################################################
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
###########################################################

# Third party imports
from botbuilder.core import ActivityHandler, CardFactory, ConversationState, MessageFactory, TurnContext
from botbuilder.core.skills import BotFrameworkSkill
from botbuilder.schema import Activity, ActivityTypes, Attachment, ChannelAccount
from botbuilder.integration.aiohttp.skills import SkillHttpClient

# Local imports
from cards import ListSkillsCard, UnknownSkillCard, WelcomeCard
from config import BotConfig, SkillConfiguration
from typing import List


ACTIVE_SKILL_PROPERTY_NAME = "activeSkillProperty"
TARGET_SKILL_ID = "EchoSkillBot"


class MainBot(ActivityHandler):
    def __init__(
        self,
        conversation_state: ConversationState,
        skills_config: SkillConfiguration,
        skill_client: SkillHttpClient,
        config: BotConfig,
    ):
        self._bot_id = config.APP_ID
        self._skill_client = skill_client
        self._skills_config = skills_config
        self._conversation_state = conversation_state
        self._active_skill_property = conversation_state.create_property(
            ACTIVE_SKILL_PROPERTY_NAME
        )


    async def on_turn(self, turn_context):
        # Forward all activities except EndOfConversation to the active skill.
        if turn_context.activity.type != ActivityTypes.end_of_conversation:
            # If there is an active skill
            active_skill: BotFrameworkSkill = await self._active_skill_property.get(
                turn_context
            )

            if active_skill:
                # If there is an active skill, forward the Activity to it.
                await self.__send_to_skill(turn_context, active_skill)
                return

        await super().on_turn(turn_context)


    async def on_message_activity(self, turn_context: TurnContext):

        skills = self._skills_config.SKILLS
        req = turn_context.activity.text.lower()

        # Call for help?
        if req.startswith("help"):

            # Generate skills list card
            card = ListSkillsCard(skills)
            cardJson = await card.genCard()

            # Create message to send
            message = Activity(
                type = ActivityTypes.message,
                attachments = [CardFactory.adaptive_card(cardJson)]
            )

            # Send response
            await turn_context.send_activity(message)


        # Call to run skill?
        elif req in skills:

            # Begin forwarding Activities to the skill
            await turn_context.send_activity(
                MessageFactory.text("Got it, connecting you to the skill...")
            )

            skill = self._skills_config.SKILLS[TARGET_SKILL_ID]
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


    async def on_end_of_conversation_activity(self, turn_context: TurnContext):
        # forget skill invocation
        await self._active_skill_property.delete(turn_context)

        eoc_activity_message = f"Received {ActivityTypes.end_of_conversation}.\n\nCode: {turn_context.activity.code}"
        if turn_context.activity.text:
            eoc_activity_message = (
                eoc_activity_message + f"\n\nText: {turn_context.activity.text}"
            )

        if turn_context.activity.value:
            eoc_activity_message = (
                eoc_activity_message + f"\n\nValue: {turn_context.activity.value}"
            )

        await turn_context.send_activity(eoc_activity_message)

        # We are back
        await turn_context.send_activity(
            MessageFactory.text(
                'Back in the root bot. Say "skill" and I\'ll patch you through'
            )
        )

        await self._conversation_state.save_changes(turn_context, force=True)


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


    async def __send_to_skill(
        self, turn_context: TurnContext, target_skill: BotFrameworkSkill
    ):
        # NOTE: Always SaveChanges() before calling a skill so that any activity generated by the skill
        # will have access to current accurate state.
        await self._conversation_state.save_changes(turn_context, force=True)

        # route the activity to the skill
        await self._skill_client.post_activity_to_skill(
            self._bot_id,
            target_skill,
            self._skills_config.SKILL_HOST_ENDPOINT,
            turn_context.activity,
        )

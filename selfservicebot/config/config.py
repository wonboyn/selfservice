###########################################################
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
###########################################################

import os


class BotConfig:
    """ Bot Configuration """

    # Callers to only those specified, '*' allows any caller.
    # Example: os.environ.get("AllowedCallers", ["54d3bb6a-3b6d-4ccd-bbfd-cad5c72fb53a"])
    ALLOWED_CALLERS = os.environ.get("AllowedCallers", ["*"])

    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    PORT = 3978
    SKILLS = [
        {
            "id": "EchoSkillBot",
            "app_id": "TODO: Add here the App ID for the skill",
            "skill_endpoint": "http://localhost:39783/api/messages",
        },
    ]
    SKILL_HOST_ENDPOINT = "http://localhost:3978/api/skills"
    SKILLS_TABLE_NAME = "skills"


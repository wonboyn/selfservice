###########################################################
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
###########################################################

import os


class BotConfig:

    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    PORT = 3978
    SKILLS_TABLE_NAME = "skills"


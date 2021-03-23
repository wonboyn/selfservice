# Third party imports
from botbuilder.core.skills import BotFrameworkSkill
import boto3

# Local imports
from config import BotConfig
from typing import Dict


# Extend the BotFrameworkSkill with a few extra attributes
class BotSkill(BotFrameworkSkill):
    
    def __init__(
        self, 
        id: str = None, 
        app_id: str = None, 
        skill_endpoint: str = None,
        category: str = None,
        description: str = None,
        docurl: str = None,
    ):
        super().__init__(id, app_id, skill_endpoint)
        self.category = category
        self.description = description
        self.docurl = docurl



class SkillConfiguration:
    SKILL_HOST_ENDPOINT = BotConfig.SKILL_HOST_ENDPOINT
    SKILLS: Dict[str, BotFrameworkSkill] = dict()

    def __init__(self):

        # Fetch skills from DynamoDB
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(BotConfig.SKILLS_TABLE_NAME)
        response = table.scan()
        items = response['Items']

        # Handle results pagination if necessary
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response['Items'])

        # Populate SKILLS class variable
        for item in items:
            id = item['name']
            desc = item['description']
            boturl = item['boturl']
            category = item['category']
            docurl = item['docurl']
            skill = BotSkill(id, '', boturl, category, desc, docurl)
            self.SKILLS[id] = skill



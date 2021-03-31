# Third party imports
import boto3

# Local imports
from config import BotConfig
from typing import Dict


# Skill class
class Skill:
    
    def __init__(
        self, 
        name: str = None, 
        description: str = None,
        category: str = None,
        lambda_name: str = None,
        docurl: str = None,
    ):
        self.category = category
        self.description = description
        self.docurl = docurl
        self.lambda_name = lambda_name
        self.name = name



class Skills:

    SKILLS: Dict[str, Skill] = dict()

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
            name = item['name']
            desc = item['description']
            lambda_name = item['boturl']
            category = item['category']
            docurl = item['docurl']
            skill = Skill(name, desc, category, lambda_name, docurl)
            self.SKILLS[name] = skill



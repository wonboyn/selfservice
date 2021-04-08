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
        self.__category = category
        self.__description = description
        self.__docurl = docurl
        self.__lambda_name = lambda_name
        self.__name = name

    def getCategory(self):
        return self.__category

    def getDesc(self):
        return self.__description

    def getDocUrl(self):
        return self.__docurl

    def getLambdaName(self):
        return self.__lambda_name

    def getSkillName(self):
        return self.__name


class Skills:

    def __init__(self):

        # Setup dictionary for skills
        self._skills: Dict[str, Skill] = dict()

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
            self._skills[name] = skill

    def getSkills(self):
        return self._skills

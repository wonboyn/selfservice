###########################################################
# This module handles retrieval of skills from
# AWS Dynamo DB.
#
###########################################################

# Third party imports
import boto3
from botocore import exceptions
import sys, traceback
from typing import Dict

# Local imports
from config import BotConfig
from constants import AwsDynamoDB, ErrorMessages, SkillItem


# Skill class
class Skill:
    """The skill class is used to represent a skill that can be called by the bot."""
    
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

    def getCategory(self) -> str:
        """Get the category of the skill."""
        return self.__category

    def getDesc(self) -> str:
        """Get the description of the skill."""
        return self.__description

    def getDocUrl(self) -> str:
        """Get the documentation url of the skill."""
        return self.__docurl

    def getLambdaName(self) -> str:
        """Get the AWS Lambda name of the skill."""
        return self.__lambda_name

    def getSkillName(self) -> str:
        """Get the name of the skill."""
        return self.__name


class Skills:
    """The skills class is used to represent all skills that can be called by the bot."""

    def __init__(self):

        # Setup dictionary for skills
        self._skills: Dict[str, Skill] = dict()

        # Fetch skills from DynamoDB
        dynamodb = boto3.resource(AwsDynamoDB.DYNAMODB)
        table = dynamodb.Table(BotConfig.SKILLS_TABLE_NAME)
        try:
            response = table.scan()
            items = response[AwsDynamoDB.ITEMS]

            # Handle results pagination if necessary
            while AwsDynamoDB.LASTEVALKEY in response:
                response = table.scan(ExclusiveStartKey=response[AwsDynamoDB.LASTEVALKEY])
                items.extend(response[AwsDynamoDB.ITEMS])

        except exceptions.ClientError as e:

            # Log details then throw the exception up the line for handling
            print(ErrorMessages.DYNAMODB_SCAN_ERROR, file=sys.stdout)
            traceback.print_exc(file=sys.stdout)
            raise

        # Populate SKILLS class variable
        for item in items:
            
            # Grab the attributes we need
            category = item[SkillItem.CATEGORY]
            desc = item[SkillItem.DESCRIPTION]
            docurl = item[SkillItem.DOC_URL]
            lambda_name = item[SkillItem.BOT_URL]
            name = item[SkillItem.NAME]

            # Populate the array
            skill = Skill(name, desc, category, lambda_name, docurl)
            self._skills[name] = skill


    def getSkills(self):
        """Get all available skills."""
        return self._skills

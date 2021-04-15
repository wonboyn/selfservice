###########################################################
# This module contains all of the fixtures used by the
# Pytest unit tests.
#
###########################################################

# Third party imports
import boto3
from moto import mock_dynamodb2
import os
import pytest
from typing import Dict

# Local imports
from src.skills import Skill


###
# Fixture to return nothing
###
@pytest.fixture(scope='function')
def gen_none():
    """Generate nothing!."""
    return None


###
# Fixture to generate a dictionary of skills
###
@pytest.fixture(scope='function')
def gen_skills_dict():
    """Generate a dictionary of skill objects."""

    skills = dict()
    skill = Skill("test", "test", "test", "test", "https://somewhere.org/test")
    skills["test"] = skill
    return skills


###
# Fixture to setup dummy AWS credentials
###
@pytest.fixture(scope='function')
def mock_aws_credentials():
    """Create mocked AWS Credentials."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_DEFAULT_REGION'] = 'ap-southeast-2'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'


###
# Fixture to create a DynamoDB client
###
@pytest.fixture(scope='function')
def mock_dynamodb_client(mock_aws_credentials):
    """Create mocked DynamoDB client."""
    with mock_dynamodb2():
        # yield boto3.resource('dynamodb', region_name='ap-southeast-2')
        yield boto3.resource('dynamodb')


###
# Fixture to create skills table in DynamoDB
###
@pytest.fixture(scope='function')
def mock_dynamodb_skills_table(mock_dynamodb_client):

    # Create the table
    table = mock_dynamodb_client.create_table(
        TableName='skills',
        KeySchema=[
            {
                'AttributeName': 'category',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'name',
                'KeyType': 'RANGE'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'category',
                'AttributeType': 'S'
            },
        ],
        BillingMode='PAY_PER_REQUEST'
    )
    
    table.meta.client.get_waiter('table_exists').wait(TableName='skills')
    yield

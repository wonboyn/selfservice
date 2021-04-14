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


###
# Fixture to setup dummy credentials
###
@pytest.fixture(scope='function')
def aws_credentials():
    """Create mocked AWS Credentials."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'


###
# Fixture to create a DynamoDB client
###
@pytest.fixture(scope='function')
def dynamodb_client(aws_credentials):
    """Create mocked DynamoDB client."""
    with mock_dynamodb2():
        yield boto3.resource('dynamodb', region_name='ap-southeast-2')


###
# Fixture to create skills table
###
@pytest.fixture(scope='function')
def dynamodb_create_skills_table(dynamodb_client):

    # Create the table
    table = dynamodb_client.create_table(
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

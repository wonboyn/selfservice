###########################################################
# This module handles testing of the skills module
#
###########################################################

# Third party imports
from botocore.exceptions import ClientError

# Local imports
from src.skills import Skills


###
# Test skills table missing
###
def test_table_missing(mock_dynamodb_client):

    try:
        Skills()
    except ClientError as err:
        assert err.response['Error']['Code'] == "ResourceNotFoundException"


###
# Test skills table exists
###
def test_table_exists(mock_dynamodb_skills_table):

    skills = Skills()
    assert skills is not None

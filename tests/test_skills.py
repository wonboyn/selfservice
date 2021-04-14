###########################################################
# This module handles testing of the skills module
#
###########################################################

# Third party imports
from botocore.exceptions import ClientError

# Local imports
from src.skills import Skills


###
# Test missing skills table
###
def test_missing_table(dynamodb_client):

    try:
        Skills()
    except ClientError as err:
        assert err.response['Error']['Code'] == "ResourceNotFoundException"

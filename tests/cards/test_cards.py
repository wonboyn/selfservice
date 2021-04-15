###########################################################
# This module handles testing of the cards modules
#
###########################################################

# Third party imports
from contextlib import nullcontext as does_not_raise
import pytest

# Local imports
from src.cards import ErrorCard, HelpCard, HelpSkillCard, UnknownSkillCard, WelcomeCard
from src.skills import Skills


###
# Test ErrorCard
###
@pytest.mark.parametrize(
    "msg,expected",
    [
        pytest.param("Some error message", does_not_raise(), id="With parameter"),
        pytest.param("", pytest.raises(Exception), id="No parameter"),
    ],
)
def test_errorcard(msg, expected):
    with expected:
        ErrorCard(msg)


###
# Test HelpCard
###
@pytest.mark.parametrize(
    "skills,expected",
    [
        pytest.param("gen_skills_dict", does_not_raise(), id="With skills"),
        pytest.param("gen_none", pytest.raises(Exception), id="No skills"),
    ],
)
def test_helpcard(skills, expected, request):
    skills = request.getfixturevalue(skills)
    with expected:
        HelpCard(skills)


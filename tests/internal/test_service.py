import unittest

from unittest.mock import MagicMock

from app.internal.service import ChurchMembersService
from app.internal.api import ChurchMembersGateway

from tests.internal import (
    MOCK_MEMBER,
    MEMBER_ID,
    TOKEN
)

class ChurchMemberServiceTestCase(unittest.TestCase):

    def __init__(self, method_name="runTest"):
        super().__init__(method_name)
        self.gateway = ChurchMembersGateway()
        self.service = ChurchMembersService(self.gateway)


    def test_get_member_success(self):
        self.gateway.get_member = MagicMock(return_value=MOCK_MEMBER)
        member = self.service.get_member(MEMBER_ID, TOKEN)
        self.assertDictEqual(member, MOCK_MEMBER)
        self.gateway.get_member.assert_called_with(MEMBER_ID, TOKEN)

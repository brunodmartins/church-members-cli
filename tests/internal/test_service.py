import unittest
from unittest.mock import MagicMock

from app.internal.api import ChurchMembersGateway
from app.internal.service import ChurchMembersService, AuthenticationService
from tests.internal import (
    MOCK_MEMBER,
    MEMBER_ID,
    TOKEN, USER, PASSWORD
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

    def test_get_member_fails(self):
        self.gateway.get_member = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.service.get_member(MEMBER_ID, TOKEN)
        self.gateway.get_member.assert_called_with(MEMBER_ID, TOKEN)


class AuthenticationServiceTestCase(unittest.TestCase):

    def __init__(self, method_name="runTest"):
        super().__init__(method_name)
        self.gateway = ChurchMembersGateway()
        self.service = AuthenticationService(self.gateway)

    def test_login_success(self):
        self.gateway.get_token = MagicMock(return_value=TOKEN)
        self.service._AuthenticationService__save_token = MagicMock()
        self.service.login(USER, PASSWORD)
        self.gateway.get_token.assert_called_with(USER, PASSWORD)
        self.service._AuthenticationService__save_token.assert_called_with(TOKEN)

    def test_login_fails(self):
        self.gateway.get_token = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.service.login(USER, PASSWORD)
        self.gateway.get_token.assert_called_with(USER, PASSWORD)

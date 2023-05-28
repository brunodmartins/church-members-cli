import unittest
from unittest.mock import MagicMock

from app.internal.api import ChurchMembersGateway
from app.internal.authentication import AuthenticationService
from app.internal.service import ChurchMembersService
from tests.internal import (
    MOCK_MEMBER,
    MEMBER_ID,
    TOKEN, USER, PASSWORD, MOCK_SEARCH
)


class ChurchMemberServiceTestCase(unittest.TestCase):

    def __init__(self, method_name="runTest"):
        super().__init__(method_name)
        self.gateway = ChurchMembersGateway()
        self.service = ChurchMembersService(self.gateway)

    def test_get_member_success(self):
        self.gateway.get_member = MagicMock(return_value=MOCK_MEMBER)
        member = self.service.get_member(MEMBER_ID, token=TOKEN)
        self.assertDictEqual(member, MOCK_MEMBER)
        self.gateway.get_member.assert_called_with(MEMBER_ID, TOKEN)

    def test_get_member_fails(self):
        self.gateway.get_member = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.service.get_member(MEMBER_ID, token=TOKEN)
        self.gateway.get_member.assert_called_with(MEMBER_ID, TOKEN)

    def test_search_member_success(self):
        self.gateway.search_member = MagicMock(return_value=MOCK_SEARCH)
        result = self.service.search_member("member-name", token=TOKEN)
        self.assertEqual(MOCK_SEARCH, result)
        self.gateway.search_member.assert_called_with("member-name", TOKEN)


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

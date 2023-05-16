import unittest
from unittest.mock import patch, MagicMock

from requests import Response

from app.internal.api import get_member
from app.internal.domain.exception import NotFoundException, ForbiddenException
from tests.internal import MOCK_HOST, MOCK_CONFIG, MEMBER_ID, TOKEN, MOCK_MEMBER


class APITestCase(unittest.TestCase):
    @patch("app.internal.api.read_config", return_value=MOCK_CONFIG)
    @patch("app.internal.api.requests")
    def test_get_member_success(self, requests, read_config):
        mock_response = Response()
        mock_response.status_code = 200
        mock_response.json = MagicMock(return_value=MOCK_MEMBER)
        requests.get.return_value = mock_response
        self.assertEqual(MOCK_MEMBER, get_member(MEMBER_ID, TOKEN))
        requests.get.assert_called_with(
            f"{MOCK_HOST}/members/{MEMBER_ID}", headers={"X-Auth-Token": TOKEN}
        )

    @patch("app.internal.api.read_config", return_value=MOCK_CONFIG)
    @patch("app.internal.api.requests")
    def test_get_member_fails(self, requests, read_config):
        test_cases = {403: ForbiddenException, 404: NotFoundException, 500: Exception}
        for status_code in test_cases.keys():
            mock_response = Response()
            mock_response.status_code = status_code
            requests.get.return_value = mock_response
            with self.assertRaises(test_cases[status_code]):
                get_member(MEMBER_ID, TOKEN)
            requests.get.assert_called_with(
                f"{MOCK_HOST}/members/{MEMBER_ID}", headers={"X-Auth-Token": TOKEN}
            )


if __name__ == "__main__":
    unittest.main()
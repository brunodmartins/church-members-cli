import base64

import requests

from app.internal.config import Configuration
from app.internal.domain.exception import ForbiddenException, NotFoundException


class ChurchMembersGateway:
    """
    A gateway to access the church-members-api via HTTP requests
    """

    def __init__(self):
        config = Configuration.read_config()
        self.host = config["host"]
        self.church_id = config["church_id"]

    def get_token(self, user: str, password: str) -> str:
        """
        Obtain an access token to a giver user
        :param user: The username
        :param password: The user password
        :return: The access token
        """

        auth_header = base64.b64encode(f"{user}:{password}".encode()).decode("utf-8")

        url = f"{self.host}/users/token"
        headers = {"church_id": self.church_id, "Authorization": f"Basic {auth_header}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            raise NotFoundException(f"User {user} not found")
        if response.status_code != 201:
            message = response.text
            raise Exception(
                f"Error doing login. Status Code: {response.status_code} Message: {message}"
            )
        return response.json()["token"]

    def get_member(self, member_id: str, token: str) -> dict:
        """
        Get a member information
        :param member_id:  The member ID
        :param token: The access token
        :return: A member information as JSON
        """
        url = f"{self.host}/members/{member_id}"
        headers = {"X-Auth-Token": token}
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            raise NotFoundException(f"Member {member_id} not found")
        if response.status_code == 403:
            raise ForbiddenException("Forbidden. Please, check login information")
        if response.status_code != 200:
            message = response.text
            raise Exception(
                f"Error getting member. Status Code: {response.status_code} Message: {message}"
            )
        return response.json()

    def search_member(self, name: str, token: str) -> list:
        """
        Search a member by
        :param name: the member name
        :param token: The access token
        :return: a list containing the members name
        """
        url = f"{self.host}/members?name={name}"
        headers = {"X-Auth-Token": token}
        response = requests.get(url, headers=headers)
        if response.status_code == 403:
            raise ForbiddenException("Forbidden. Please, check login information")
        if response.status_code != 200:
            message = response.text
            raise Exception(
                f"Error searching member. Status Code: {response.status_code} Message: {message}"
            )
        return response.json()

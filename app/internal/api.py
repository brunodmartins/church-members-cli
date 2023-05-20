import base64

import requests

from app.internal.config import Configuration
from app.internal.domain.exception import ForbiddenException, NotFoundException


class ChurchMembersGateway:
    def get_token(self, user, password):
        config = Configuration.read_config()
        host = config["host"]
        church_id = config["church_id"]

        auth_header = base64.b64encode(f"{user}:{password}".encode()).decode("utf-8")

        url = f"{host}/users/token"
        headers = {"church_id": church_id, "Authorization": f"Basic {auth_header}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            raise NotFoundException(f"User {user} not found")
        if response.status_code != 201:
            message = response.text
            raise Exception(
                f"Error doing login. Status Code: {response.status_code} Message: {message}"
            )
        return response.json()["token"]

    def get_member(self, member_id, token):
        config = Configuration.read_config()
        host = config["host"]
        url = f"{host}/members/{member_id}"
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

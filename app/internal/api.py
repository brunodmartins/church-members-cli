import requests

from app.internal.config import read_config
from app.internal.domain.exception import ForbiddenException, NotFoundException


def get_token(user, password):
    config = read_config()
    host = config["host"]
    church_id = config["church_id"]
    session = requests.Session()
    session.auth = (user, password)

    url = f"{host}/users/token"
    headers = {"church_id": church_id}
    response = session.get(url, headers=headers)
    if response.status_code == 404:
        raise NotFoundException(f"User {user} not found")
    if response.status_code != 201:
        message = response.text
        raise Exception(
            f"Error doing login. Status Code: {response.status_code} Message: {message}"
        )
    return response.json()["token"]


def get_member(member_id, token):
    config = read_config()
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

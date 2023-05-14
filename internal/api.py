import requests

from internal.config import read_config


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
        raise Exception("User not found")
    if response.status_code != 201:
        message = response.text
        raise Exception(f"Error doing login: {message}")
    return response.json()["token"]


def get_member(member_id, token):
    config = read_config()
    host = config["host"]
    church_id = config["church_id"]
    url = f"{host}/members/{member_id}"
    headers = {"X-Auth-Token": token}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        raise Exception("Member not found")
    if response.status_code != 200:
        message = response.text
        raise Exception(f"Error getting member: {message}")
    return response.json()

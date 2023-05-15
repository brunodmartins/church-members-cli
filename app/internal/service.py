from app.internal import api
from app.internal.config import CONFIG_FOLDER


def login(user, password):
    token = api.get_token(user, password)
    save_token(token)


def save_token(token):
    with open(f"{CONFIG_FOLDER}/token", "w") as f:
        f.write(token)


def get_token():
    with open(f"{CONFIG_FOLDER}/token", "r") as f:
        return f.readline()


def get_member(member_id):
    print(api.get_member(member_id, get_token()))

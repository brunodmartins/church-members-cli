from app.internal.api import ChurchMembersGateway
from app.internal.config import CONFIG_FOLDER


class ChurchMembersService:
    def __init__(self, gateway: ChurchMembersGateway = None):
        self.gateway = gateway

    def get_member(self, member_id):
        print(self.gateway.get_member(member_id, get_token()))


class AuthenticationService:
    def __init__(self, gateway: ChurchMembersGateway = None):
        self.gateway = gateway

    def login(self, user, password):
        token = ChurchMembersGateway().get_token(user, password)
        self.save_token(token)

    def save_token(self, token):
        with open(f"{CONFIG_FOLDER}/token", "w") as f:
            f.write(token)

    def get_token(self):
        with open(f"{CONFIG_FOLDER}/token", "r") as f:
            return f.readline()

from app.internal.api import ChurchMembersGateway
from app.internal.config import CONFIG_FOLDER


class ChurchMembersService:
    def __init__(self, gateway: ChurchMembersGateway = None):
        self.gateway = gateway

    def get_member(self, member_id, token):
        print(self.gateway.get_member(member_id, token))


class AuthenticationService:
    def __init__(self, gateway: ChurchMembersGateway = None):
        self.gateway = gateway

    def login(self, user, password):
        token = ChurchMembersGateway().get_token(user, password)
        self.__save_token(token)

    @staticmethod
    def __save_token(token):
        with open(f"{CONFIG_FOLDER}/token", "w") as f:
            f.write(token)

    def get_token(self):
        with open(f"{CONFIG_FOLDER}/token", "r") as f:
            return f.readline()

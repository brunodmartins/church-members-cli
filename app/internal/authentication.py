from app.internal.api import ChurchMembersGateway
from app.internal.config import CONFIG_FOLDER


class AuthenticationService:
    """
    Contains operations related to the user authentication
    """

    def __init__(self, gateway: ChurchMembersGateway):
        self.gateway = gateway

    def login(self, user: str, password: str) -> None:
        """
        Performs user authentication
        :param user: The user
        :param password: The password
        """
        token = self.gateway.get_token(user, password)
        self.__save_token(token)

    @staticmethod
    def get_token() -> str:
        """
        Reads a user session token
        :return: the user token1
        """
        with open(f"{CONFIG_FOLDER}/token", "r") as f:
            return f.readline()

    @staticmethod
    def __save_token(token: str) -> None:
        """
        Save an access token
        :param token: The access token
        """
        with open(f"{CONFIG_FOLDER}/token", "w") as f:
            f.write(token)


def require_token(func):
    def decorator(*args, **kw):
        token = AuthenticationService.get_token()
        if "token" not in kw:
            kw["token"] = token
        return func(*args, **kw)

    return decorator

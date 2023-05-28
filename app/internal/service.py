
from app.internal.api import ChurchMembersGateway
from app.internal.authentication import require_token


class ChurchMembersService:
    """
    A service class containing operations related to members
    """

    def __init__(self, gateway: ChurchMembersGateway):
        self.gateway = gateway

    @require_token
    def get_member(self, member_id: str, token: str) -> dict:
        """
        Gets a member
        :param member_id: The member ID
        :param token: Access token
        :return: a member object
        """
        return self.gateway.get_member(member_id, token)

    def search_member(self, member_name: str, token: str) -> dict:
        """
        Search a member
        :param member_name: The member name
        :param token: Access token
        :return: a member object
        """
        return self.gateway.search_member(member_name, token)

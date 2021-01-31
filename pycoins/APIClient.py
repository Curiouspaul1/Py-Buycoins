from exc import MissingKeyError
from base64 import b64encode
from actions.buy import Buycoins


class PycoinsClient:
    """
    Handles requests
    """

    _URL = "https://backend.buycoins.tech/api/graphql"

    def __init__(self, public_key=None, secret_key=None):
        if not public_key:
            raise MissingKeyError("Missing Public_key")
        if not secret_key:
            raise MissingKeyError("Missing secret_key")
        api_key = b64encode(f"{public_key}:{secret_key}".encode('utf-8'))
        self.API_KEY = api_key.decode('utf-8')

    def set_headers(self):
        return {
            "Authorization": f"Basic {self.API_KEY}"
        }

    def buy(self):
        """
        buy coins
        """
        pass

    def sell(self):
        """
        sell coins
        """
        pass

    def send(self):
        """
        send coins
        """
        pass

    def receive(self):
        """
        receive coins
        """

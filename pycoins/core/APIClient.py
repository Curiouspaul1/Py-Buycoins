from exc import MissingKeyError
from base64 import b64encode
from buy import Buycoins
from typing import Optional, List
import requests


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

    def buy(self, subfields: List, fields: List[tuple], from_buycoins: Optional[bool] = True):
        """
        buy coins
        """
        headers = self.set_headers()
        if from_buycoins is True:
            _order = Buycoins()._buy(
                fields=fields,
                subfields=subfields
            )
            _req = requests.post(
                url=PycoinsClient._URL,
                json={"query": _order},
                headers=headers
            )
            return _req.json()
        else:
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


client = PycoinsClient(public_key="I_8roV2FBaA",secret_key="n3n0CA3Zf3z1ADhAwUMv0CkeXt-xQqYP5Z31i0iGxA4")
print(client.buy(
    fields=[
        (
            "price","QnV5Y29pbnNQcmljZS0zOGIwYTg1Yi1jNjA1LTRhZjAtOWQ1My01ODk1MGVkMjUyYmQ="
        ),
        (
            "coin_amount", 0.002
        ),
        (
            "cryptocurrency", "bitcoin"
        )
    ],
    subfields=[
        "id",
        "cryptocurrency",
        "status",
        "totalCoinAmount"
    ]
))
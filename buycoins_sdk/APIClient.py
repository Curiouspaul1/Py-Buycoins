from exc import MissingKeyError
from naira_token_account import NairaTokenAccount
from send import Send
from orders import BuyCoins
from base64 import b64encode
from typing import Optional, List
import requests


class BuyCoinsClient:
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

    def execute(self, query):
        headers = self.set_headers()
        _req = requests.post(
            json={"query": query},
            url=BuyCoinsClient._URL,
            headers=headers
        )
         
        if _req.status_code == 200:
            return (_req.text, _req.status_code)
        else:
            print(_req)


client = BuyCoinsClient(public_key="I_8roV2FBaA",secret_key="n3n0CA3Zf3z1ADhAwUMv0CkeXt-xQqYP5Z31i0iGxA4")
q = Send()._send('bitcoin', 0.03, "1MmyYvSEYLCPm45Ps6vQin1heGBv3UpNbf", subfields=["id", "address", "status"])
print(client.execute(query=q))
from exc import MissingKeyError
from base64 import b64encode
from buy import Buycoins
from sell import Sellcoins
from send import Send
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

    def getSalePrice(self, subfields: List):
        headers = self.set_headers()
        getprice = Buycoins().getSalePrice(subfields=subfields)
        _req = requests.post(
            json={"query": getprice},
            url=PycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)

    def createDepositAcct(self, fields: List[tuple], subfields: List):
        headers = self.set_headers()
        new_acct = Buycoins().createAccount(fields=fields, subfields=subfields)
        _req = requests.post(
            json={"query": new_acct},
            url=PycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)
    
    def getEstimatedNetworkFee(self, subfields: List):
        headers = self.set_headers()
        new_transaction = Send().getNetworkFee(subfields=subfields)
        _req = requests.post(
            json={"query": new_transaction},
            url=PycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)

    def buy(self, subfields: List, price: str, coin_amount: float, cryptocurrency, from_buycoins: Optional[bool] = True):
        """
        buy coins
        """
        headers = self.set_headers()
        if from_buycoins is True:
            buy_instance = Buycoins()
            _order = buy_instance._buy(
                subfields=subfields,
                price=price,
                coin_amount=coin_amount,
                cryptocurrency=cryptocurrency
            )
            print(_order)
            _req = requests.post(
                url=PycoinsClient._URL,
                json={"query": _order},
                headers=headers
            )
            return (_req.json(), _req.status_code)
        else:
            # TODO: P2P trading
            pass

    def sell(self, subfields: List, price: str, coin_amount: float, cryptocurrency, to_buycoins: Optional[bool] = True):
        """
        sell coins
        """
        headers = self.set_headers()
        if to_buycoins is True:
            sell_instance = Sellcoins()
            _order = sell_instance._sell(
                subfields=subfields,
                price=price,
                coin_amount=coin_amount,
                cryptocurrency=cryptocurrency
            )
            print(_order)
            _req = requests.post(
                url=PycoinsClient._URL,
                json={"query": _order},
                headers=headers
            )
            return (_req.json(), _req.status_code)
        else:
            # TODO: P2P trading
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
print(client.getSalePrice(["id","cryptocurrency","sellPricePerCoin"]))
print(client.buy(
    subfields=[
        "id",
        "cryptocurrency",
        "status",
        "totalCoinAmount"
    ],
    price="QnV5Y29pbnNQcmljZS0zOGIwYTg1Yi1jNjA1LTRhZjAtOWQ1My01ODk1MGVkMjUyYmQ=",
    coin_amount=0.002,
    cryptocurrency="bitcoin"
))
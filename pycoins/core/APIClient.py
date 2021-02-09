#from exc import MissingKeyError
from .exc import MissingKeyError
from base64 import b64encode
from .buy import Buycoins, BuycoinsP2P
from .sell import Sellcoins
from .send import Send
from .receive import Receive
from typing import Optional, List
import requests


class BuycoinsClient:
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
            url=BuycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)

    def createAddress(self, cryptocurrency, subfields):
        headers = self.set_headers()
        new_address = Receive().create_address(
            cryptocurrency,
            subfields
        )
        _req = requests.post(
            json={"query": new_address},
            headers=headers,
            url=BuycoinsClient._URL
        )
        return (_req.json(), _req.status_code)

    def getDynamicprice(self, status):
        headers = self.set_headers()
        price = BuycoinsP2P().getDynamicPrice(
            status=status
        )
        _req = requests.post(
            json={"query": price},
            url=PycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)

    def getOrders(self, status, subfields: List):
        headers = self.set_headers()
        getdate = BuycoinsP2P().getOrders(
            status=status, subfields=subfields
            )
        _req = requests.post(
            json={"query": getdate},
            url=BuycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)

    def getMarketBook(self, status, subfields: List) -> str:
        headers = self.set_headers()
        market_book = BuycoinsP2P().getMarketBook(
            status=status
        ).queryObject(subfields=subfields)
        _req = requests.post(
            json={"query": market_book},
            url=PycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)

    def createDepositAcct(self, fields: List[tuple], subfields: List):
        headers = self.set_headers()
        new_acct = Buycoins().createAccount(fields=fields, subfields=subfields)
        _req = requests.post(
            json={"query": new_acct},
            url=BuycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)
    
    def getEstimatedNetworkFee(self, subfields: List):
        headers = self.set_headers()
        new_transaction = Send().getNetworkFee(subfields=subfields)
        _req = requests.post(
            json={"query": new_transaction},
            url=BuycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)

    def getBalance(self, subfields: List, args: Optional[List[tuple]]=None):
        headers = self.set_headers()
        _req = requests.post(
            url=BuycoinsClient._URL,
            json={
                "query": Send()._balance(
                    args=args,
                    subfields=subfields
                )
            },
            headers=headers
        )
        return (_req.json(), _req.status_code)

    def buy(self, subfields: List, price: str, coin_amount: float, cryptocurrency):
        """
        Direct purchase from BuyCoins
        """
        headers = self.set_headers()
        buy_instance = Buycoins()
        _order = buy_instance._buy(
            subfields=subfields,
            price=price,
            coin_amount=coin_amount,
            cryptocurrency=cryptocurrency
        )
        print(_order)
        _req = requests.post(
            url=BuycoinsClient._URL,
            json={"query": _order},
            headers=headers
        )
        return (_req.json(), _req.status_code)


    def post_limit_order(self, subfields: List, order_side: str, coin_amount: float, cryptocurrency, price_type: str, price_type_value: Optional[List[tuple]]=None):
        """
        p2p purchase
        """
        headers = self.set_headers()
        _post = BuycoinsP2P()
        _order = _post.limit_order(
            subfields=subfields,
            order_side=order_side,
            coin_amount=coin_amount,
            cryptocurrency=cryptocurrency,
            price_type=price_type,
            price_type_value=price_type_value
            )

        _req = requests.post(
            url=BuycoinsClient._URL,
            json={"query": _order},
            header=headers
        )
        return (_req.json(), _req.status_code)

    def post_market_order(self, subfields: List, order_side: str, coin_amount: float, cryptocurrency: str):
        headers = self.set_headers()
        _post = BuycoinsP2P()
        _order = _post.market_order(
            subfields=subfields,
            order_side=order_side,
            coin_amount=coin_amount,
            cryptocurrency=cryptocurrency
        )
        _req = requests.post(
            url=BuycoinsClient._URL,
            json={"query", _order},
            header=headers
        )
        return (_req.json(), _req.status_code)

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
                url=BuycoinsClient._URL,
                json={"query": _order},
                headers=headers
            )
            return (_req.json(), _req.status_code)
        else:
            pass

    def send(self, amount, cryptocurrency, address, subfields: List):
        """
        send coins
        """
        headers = self.set_headers()
        new_send = Send()._send(
            amount=amount,
            cryptocurrency=cryptocurrency,
            address=address,
            subfields=subfields
        )
        _req = requests.post(
            json={"query": new_send},
            url=BuycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)

    def receive(self):
        """
        receive coins
        """

'''
client = BuycoinsClient(public_key="I_8roV2FBaA",secret_key="n3n0CA3Zf3z1ADhAwUMv0CkeXt-xQqYP5Z31i0iGxA4")
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
'''
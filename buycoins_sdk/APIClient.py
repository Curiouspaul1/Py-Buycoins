#from exc import MissingKeyError
from exc import MissingKeyError
from base64 import b64encode
from buy import Buycoins, BuycoinsP2P
from sell import Sellcoins
from send import Send
from receive import Receive
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

    #def send_custom_request(self, fields):

    def set_headers(self):
        return {
            "Authorization": f"Basic {self.API_KEY}"
        }

    def get_sale_price(self, subfields: Optional[List]=None, cryptocurrency: Optional[str]=None):
        headers = self.set_headers()
        if cryptocurrency:
            if subfields:
                getprice = Buycoins().getSalePrice(cryptocurrency=cryptocurrency, subfields=subfields)
                _req = requests.post(
                    json={"query": getprice},
                    url=BuycoinsClient._URL,
                    headers=headers
                )
            else:
                getprice = Buycoins().getSalePrice(cryptocurrency=cryptocurrency)
                _req = requests.post(
                    json={"query": getprice},
                    url=BuycoinsClient._URL,
                    headers=headers
                )
            if _req.status_code == 200:
                return _req.json()['data']['getPrices'][0]
        else:
            if subfields:
                getprice = Buycoins().getSalePrice(subfields=subfields)
                _req = requests.post(
                    json={"query": getprice},
                    url=BuycoinsClient._URL,
                    headers=headers
                )
            else:
                getprice = Buycoins().getSalePrice()
                _req = requests.post(
                    json={"query": getprice},
                    url=BuycoinsClient._URL,
                    headers=headers
                )
            if _req.status_code == 200:
                return _req.json()['data']['getPrices']

    def create_address(self, cryptocurrency, subfields):
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

    def get_dynamic_price(self, status):
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

    def get_orders(self, status, subfields: List):
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

    def get_market_book(self, status, subfields: List) -> str:
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

    def create_deposit_account(self, fields: List[tuple], subfields: List):
        headers = self.set_headers()
        new_acct = Buycoins().createAccount(fields=fields, subfields=subfields)
        _req = requests.post(
            json={"query": new_acct},
            url=BuycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)
    
    def get_network_fee(self, subfields: List):
        headers = self.set_headers()
        new_transaction = Send().getNetworkFee(subfields=subfields)
        _req = requests.post(
            json={"query": new_transaction},
            url=BuycoinsClient._URL,
            headers=headers
        )
        return (_req.json(), _req.status_code)

    def get_balance(self, subfields: List, args: Optional[List[tuple]]=None):
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

    def buy(self, coin_amount: float, cryptocurrency, subfields: Optional[List]=None):
        """
        Direct purchase from BuyCoins
        """
        headers = self.set_headers()
        buy_instance = Buycoins()
        print(self.get_sale_price(cryptocurrency=cryptocurrency))
        if subfields:
            _order = buy_instance._buy(
                subfields=subfields,
                price=self.get_sale_price(cryptocurrency=cryptocurrency)['id'],
                coin_amount=coin_amount,
                cryptocurrency=cryptocurrency
            )
        else:
            _order = buy_instance._buy(
                price=self.get_sale_price(cryptocurrency=cryptocurrency)['id'],
                coin_amount=coin_amount,
                cryptocurrency=cryptocurrency
            )
        print(_order)
        _req = requests.post(
            url=BuycoinsClient._URL,
            json={"query": _order},
            headers=headers
        )
        if _req.status_code == 200:
            return _req.json()


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


# client = BuycoinsClient(public_key="I_8roV2FBaA",secret_key="n3n0CA3Zf3z1ADhAwUMv0CkeXt-xQqYP5Z31i0iGxA4")
# # print(client.get_sale_price(
# #         [
# #             "id","cryptocurrency",
# #             "sellPricePerCoin"
# #         ],
# #         cryptocurrency='bitcoin'
# #     )
# # )
# print(client.buy(
#     coin_amount=0.002,
#     cryptocurrency="bitcoin",
#     subfields=[
#         "id",
#         "cryptocurrency",
#         "status",
#         "totalCoinAmount"
#     ]
# ))


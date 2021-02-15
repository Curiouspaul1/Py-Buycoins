from exc import MissingKeyError
# from p2p import BuyCoinsP2P
from sending import Send
from orders import BuyCoins, SellCoins, OrdersBase
from naira_token_account import NairaTokenAccount
from receive import Receive
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
            return (_req.json(), _req.status_code)
        else:
            print(_req)


client = BuyCoinsClient(public_key="I_8roV2FBaA",secret_key="n3n0CA3Zf3z1ADhAwUMv0CkeXt-xQqYP5Z31i0iGxA4")
# P2P
# q = BuyCoinsP2P().get_market_book(response_fields=['id', 'cryptocurrency', 'coinAmount', 'side', 'status', 'createdAt', 'pricePerCoin', 'priceType', 'staticPrice', 'dynamicExchangeRate'])
# q = BuyCoinsP2P().post_limit_order('buy', 0.01, 'bitcoin', 'static', response_fields=['id', 'cryptocurrency', 'coinAmount', 'side', 'status', 'createdAt', 'pricePerCoin', 'priceType', 'dynamicExchangeRate'], static_price=60000)
# q = BuyCoinsP2P().post_market_order('buy', 0.01, 'bitcoin', response_fields=['id', 'cryptocurrency', 'coinAmount', 'side', 'status', 'createdAt', 'pricePerCoin', 'priceType', 'dynamicExchangeRate'])
buy = BuyCoins(
    coin_amount=0.02,
    price="QnV5Y29pbnNQcmljZS03MGRiYTk0ZS0zMjUwLTQ5ZTMtYjIzOS0yMzgxMWU1ZjJmYTM=",
    cryptocurrency="bitcoin"
)
resp = buy.execute(client=client)
q1 = buy.get_prices(['id', 'cryptocurrency', 'buyPricePerCoin', 'minBuy', 'maxBuy', 'expiresAt'])
q2 = buy.from_buycoins(response_fields=['id', 'cryptocurrency', 'status', 'totalCoinAmount', 'side'])
#q = SellCoins().sell("QnV5Y29pbnNQcmljZS0zOGIwYTg1Yi1jNjA1LTRhZjAtOWQ1My01ODk1MGVkMjUyYmQ=", 0.02, 'bitcoin', response_fields=['id', 'cryptocurrency', 'status', 'totalCoinAmount', 'side'])

# Sending
# q = Send().get_network_fee('bitcoin', 0.01, response_fields=['estimatedFee', 'total'])
# q = Send().check_limit(100, 'bitcoin')
# q = Send().send('bitcoin', 0.001, "1MmyYvSEYLCPm45Ps6vQin1heGBv3UpNbf", response_fields=['id', 'address', 'amount', 'cryptocurrency', 'fee', 'status'])
# q = Send().balance(response_fields=['id', 'cryptocurrency', 'confirmedBalance'])

# Naira Token Account
# q = NairaTokenAccount().create_account("tony stark", response_fields=['accountNumber', 'accountName', 'accountType', 'bankName', 'accountReference'])

# Create Address
# q = Receive().create_address('bitcoin', ['cryptocurrency' , 'address'])
# print(q)
print(client.execute(query=q1))
print(client.execute(query=q2))


#print(client.get_active_prices(response_fielraise InvalidClientObject("<BuyCoinsClient> object expected received {} instead".format(type(client)))ds=['id', 'cryptocurrency']))
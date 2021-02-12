from exc import MissingKeyError
# from p2p import BuyCoinsP2P
from sending import Send
from orders import BuyCoins, SellCoins
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
# q = BuyCoinsP2P().get_market_book(subfields=['id', 'cryptocurrency', 'coinAmount', 'side', 'status', 'createdAt', 'pricePerCoin', 'priceType', 'staticPrice', 'dynamicExchangeRate'])
# q = BuyCoinsP2P().post_limit_order('buy', 0.01, 'bitcoin', 'static', subfields=['id', 'cryptocurrency', 'coinAmount', 'side', 'status', 'createdAt', 'pricePerCoin', 'priceType', 'dynamicExchangeRate'], static_price=60000)
# q = BuyCoinsP2P().post_market_order('buy', 0.01, 'bitcoin', subfields=['id', 'cryptocurrency', 'coinAmount', 'side', 'status', 'createdAt', 'pricePerCoin', 'priceType', 'dynamicExchangeRate'])

# Orders from BuyCoins
# q = BuyCoins().get_prices(['id', 'cryptocurrency', 'buyPricePerCoin', 'minBuy', 'maxBuy', 'expiresAt'])
# q = BuyCoins().buy("QnV5Y29pbnNQcmljZS0zOGIwYTg1Yi1jNjA1LTRhZjAtOWQ1My01ODk1MGVkMjUyYmQ=", 0.02, 'bitcoin', subfields=['id', 'cryptocurrency', 'status', 'totalCoinAmount', 'side'])
# q = SellCoins().sell("QnV5Y29pbnNQcmljZS0zOGIwYTg1Yi1jNjA1LTRhZjAtOWQ1My01ODk1MGVkMjUyYmQ=", 0.02, 'bitcoin', subfields=['id', 'cryptocurrency', 'status', 'totalCoinAmount', 'side'])

# Sending
# q = Send().get_network_fee('bitcoin', 0.01, subfields=['estimatedFee', 'total'])
# q = Send().check_limit(100, 'bitcoin')
# q = Send().send('bitcoin', 0.001, "1MmyYvSEYLCPm45Ps6vQin1heGBv3UpNbf", subfields=['id', 'address', 'amount', 'cryptocurrency', 'fee', 'status'])
# q = Send().balance(subfields=['id', 'cryptocurrency', 'confirmedBalance'])

# Naira Token Account
# q = NairaTokenAccount().create_account("tony stark", subfields=['accountNumber', 'accountName', 'accountType', 'bankName', 'accountReference'])

# Create Address
# q = Receive().create_address('bitcoin', ['cryptocurrency' , 'address'])
print(q)
print(client.execute(query=q))
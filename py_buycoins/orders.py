from .gcore.queries import GetOrders, GetMarketBook, GetPrices
from .gcore.mutations import Buy, Sell
from typing import List, Optional
from .exc import InvalidClientObject


def get_prices(
    self, response_fields: List,
    cryptocurrency:  Optional[str]=None
) -> str:
    if cryptocurrency:
        return GetPrices().queryObject(
            cryptocurrency=cryptocurrency,
            response_fields=response_fields
        )
    else:
        return GetPrices().queryObject(
            response_fields=response_fields
        )


# Buying crytocurrency from Buycoins
class BuyCoins:
    def __init__(self, price: str, coin_amount: float, cryptocurrency):
        self.coin_amount = coin_amount
        self.cryptocurrency = cryptocurrency
        self.price = price

    def from_buycoins(self, response_fields) -> str:
        return Buy().Mutate(
            price=self.price,
            coin_amount=self.coin_amount,
            cryptocurrency=self.cryptocurrency,
            response_fields=response_fields
        )
    
    def execute(self, client):
        try:
            return client.execute(query=self.from_buycoins(
                response_fields=[
                    'id', 'cryptocurrency', 'status', 
                    'totalCoinAmount', 'side'
                ]
            ))
        except AttributeError:
            raise InvalidClientObject("<BuyCoinsClient> object expected received {} instead".format(type(client)))

class SellCoins:
    def __init__(self, price: str, coin_amount: float, cryptocurrency):
        self.coin_amount = coin_amount
        self.cryptocurrency = cryptocurrency
        self.price = price
    
    def sell(self, response_fields) -> str:
        return Sell().Mutate(
            coin_amount=self.coin_amount,
            price=self.price,
            response_fields=response_fields,
            cryptocurrency=self.cryptocurrency
        )

    def execute(self, client):
        try:
            return client.execute(query=self.sell())
        except AttributeError:
            raise InvalidClientObject("<BuyCoinsClient> object expected received {} instead".format(type(client)))

from gcore.queries import GetOrders, GetMarketBook, GetPrices
from gcore.mutations import Buy, Sell
from typing import List, Optional

class OrdersBase:
    def get_prices(self, subfields: List) -> str:
        return GetPrices().queryObject(
            subfields=subfields
        )


# Buying crytocurrency from Buycoins
class BuyCoins(OrdersBase):
    def buy(self, price: str, coin_amount: float, cryptocurrency, subfields: Optional[List]=None) -> str:
        return Buy().Mutate(
            price=price,
            coin_amount=coin_amount,
            cryptocurrency=cryptocurrency,
            subfields=subfields
        )
        

class SellCoins(OrdersBase):
    def sell(self, price: str, coin_amount: float, cryptocurrency: str, subfields: List) -> str:
        return Sell().Mutate(
            coin_amount=coin_amount,
            price=price,
            subfields=subfields,
            cryptocurrency=cryptocurrency
        )

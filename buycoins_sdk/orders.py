from gcore.queries import GetOrders, GetMarketBook, GetSalePrice
from gcore.mutations import Buy
from typing import List, Optional

print(Buy)
class OrdersBase:
    def __init__(self):
        self.from_buycoins = None

    def get_prices(self, subfields: Optional[List]=None, cryptocurrency: Optional[str]=None) -> str:
            return GetSalePrice().queryObject(
                cryptocurrency=cryptocurrency,
                subfields=subfields
            )


# Buying crytocurrency from Buycoins
class BuyCoins(OrdersBase):
    def __init__(self):
        super().__init__()
    
    def buy(self, price: str, coin_amount: float, cryptocurrency, subfields: Optional[List]=None) -> str:
        if subfields:
            order = Buy().Mutate(
                coin_amount=coin_amount,
                price=price,
                subfields=subfields,
                cryptocurrency=cryptocurrency
            )
            return order
        else:
            order = Buy.Mutate(
                coin_amount=coin_amount,
                price=price,
                cryptocurrency=cryptocurrency
            )
            return order



class SellCoins(OrdersBase):
    def __init__(self):
        super().__init__()

    def sell(self, subfields: List, price: str, coin_amount: float, cryptocurrency) -> str:
        order = Sell(
            coin_amount=coin_amount,
            price=price,
            subfields=subfields,
            cryptocurrency=cryptocurrency
        )
        return order.Mutate()

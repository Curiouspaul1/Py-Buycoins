from gcore.mutations import createDepositAccount, Buy, PostLimitOrder, PostMarketOrder
from gcore.queries import GetsalePrice, GetOrders, GetMarketBook, GetDynamicPriceExpiry
from typing import List, Optional


class Buybase:
    def __init__(self):
        self.from_buycoins = None

    def createAccount(self, fields: List[tuple], subfields: List) -> str:
        new_acct = createDepositAccount()
        acct = new_acct.Mutate(fields, subfields)
        return acct

    def getSalePrice(self, subfields: List, cryptocurrency: Optional[str]=None) -> str:
        if cryptocurrency:
            return GetsalePrice().queryObject(
                cryptocurrency=cryptocurrency,
                subfields=subfields
            )
        else:
            return GetsalePrice().queryObject(
                subfields=subfields
            )


# Buying from Buycoins
class Buycoins(Buybase):
    def __init__(self):
        super().__init__()

    def _buy(self, subfields: List, price: str, coin_amount: float, cryptocurrency) -> str:
        order = Buy(
            coin_amount=coin_amount,
            price=price,
            subfields=subfields,
            cryptocurrency=cryptocurrency
        )
        return order.Mutate()


# P2P purchase
class BuycoinsP2P(Buybase):
    def __init__(self):
        super().__init__()
    
    def getDynamicPrice(self, status: str) -> str:
        return GetDynamicPriceExpiry(
            status=status
        ).queryObject()

    def getOrders(self, status: str, subfields: List) -> str:
        return GetOrders(
            status=status
        ).queryObject(subfields=subfields)

    def getMarketBook(self, status: str, subfields: List) -> str:
        return GetMarketBook(
            status=status
        ).queryObject(subfields=subfields)

    def limit_order(self, subfields: List, order_side: str, coin_amount: float, cryptocurrency, price_type: str, price_type_value: Optional[List[tuple]]=None):
        order = PostLimitOrder(
            subfields=subfields,
            order_side=order_side,
            coin_amount=coin_amount,
            cryptocurrency=cryptocurrency,
            price_type=price_type,
            price_type_value=price_type_value
        )
        return order.Mutate()

    
    def market_order(self, subfields: List, order_side: str, coin_amount: float, cryptocurrency: str):
        order = PostMarketOrder(
            subfields=subfields,
            order_side=order_side,
            coin_amount=coin_amount,
            cryptocurrency=cryptocurrency
        )
        return order.Mutate()
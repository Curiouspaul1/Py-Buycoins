from gcore.mutations import createDepositAccount, Buy, PostLimitOrder
from gcore.queries import GetsalePrice, GetDynamicPriceExpiry
from typing import List


class Buybase:
    def __init__(self):
        self.from_buycoins = None

    def createAccount(self, fields: List[tuple], subfields: List) -> str:
        new_acct = createDepositAccount()
        acct = new_acct.Mutate(fields, subfields)
        return acct

    def getSalePrice(self, subfields: List) -> str:
        return GetsalePrice().queryObject(
            subfields=subfields
        )

    def getDynamicPrice(self, subfields: List) -> str:
        return GetDynamicPriceExpiry().queryObject(
            subfields=subfields
        )


# Buying from Buycoins
class Buycoins(Buybase):
    def __init__(self):
        super().__init__()
        self.from_buycoins = True

    def _buy(self, subfields: List, price: str, coin_amount: float, cryptocurrency) -> str:
        order = Buy(
            coin_amount=coin_amount,
            price=price,
            subfields=subfields,
            cryptocurrency=cryptocurrency
        )
        return order.Mutate()


# P2P trading
class BuycoinsP2P(Buybase):
    def __init__(self):
        super().__init__()
        self.from_buycoins = False

    def _buyp2p(self, subfields: List, order_side: str, coin_amount: float, cryptocurrency, price_type: str, price_type_value: Optional[List[tuple]]=None):
        order = PostLimitOrder(
            subfields=subfields,
            order_side=order_side,
            coin_amount=coin_amount,
            cryptocurrency=cryptocurrency,
            price_type=price_type,
            price_type_value=price_type_value
        )
        return order.Mutate()

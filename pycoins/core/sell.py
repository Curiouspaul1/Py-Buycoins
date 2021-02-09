from core.gcore.mutations import createDepositAccount, Sell
from core.gcore.queries import GetsalePrice
from typing import List


class Sellbase:
    def __init__(self):
        self.to_buycoins = None

    def createAccount(self, fields: List[tuple], subfields: List) -> str:
        new_acct = createDepositAccount()
        acct = new_acct.Mutate(fields, subfields)
        return acct

    def getSalePrice(self, subfields: List) -> str:
        return GetsalePrice().queryObject(
            subfields=subfields
        )


class Sellcoins(Sellbase):
    def __init__(self):
        super().__init__()
        self.to_buycoins = True

    def _sell(self, subfields: List, price: str, coin_amount: float, cryptocurrency) -> str:
        order = Sell(
            coin_amount=coin_amount,
            price=price,
            subfields=subfields,
            cryptocurrency=cryptocurrency
        )
        return order.Mutate()

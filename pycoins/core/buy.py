from gcore.mutations import createDepositAccount, Buy
from gcore.queries import GetsalePrice
from typing import List


class Buybase:
    def __init__(self):
        self.from_buycoins = None

    def createAccount(self, fields: List[tuple], subfields: List) -> str:
        new_acct = createDepositAccount()
        acct = new_acct.Mutate(fields, subfields)
        return acct

    def getSalePrice(self, subfields: List) -> str:
        return GetsalePrice(
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

    
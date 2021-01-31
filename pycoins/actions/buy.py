from graphqlcore.mutations import createDepositAccount, Buy
from graphqlcore.queries import GetsalePrice
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

    def _buy(self, fields: List[tuple], subfields: List) -> str:
        order = Buy().Mutate(
            fields=fields,
            subfields=subfields
        )
        return order

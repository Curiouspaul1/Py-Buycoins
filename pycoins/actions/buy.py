from pygraphql import createDepositAccount
from typing import List


class Buybase:
    def createAccount(self, fields: List[tuple], subfields: List):
        new_acct = createDepositAccount()
        acct = new_acct.Mutate(fields, subfields)
        return acct


# Buying from Buycoins
class Buycoins(Buybase):
    pass

from gcore.mutations import CreateDepositAccount
from typing import List, Optional


class NairaTokenAccount():


    def create_account(self, fields: List[tuple], subfields: List) -> str:
        new_acct = CreateDepositAccount()
        acct = new_acct.Mutate(fields, subfields)
        return acct

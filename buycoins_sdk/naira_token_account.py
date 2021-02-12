from gcore.mutations import CreateDepositAccount
from typing import List, Optional


class NairaTokenAccount():
    def create_account(self, accountName, subfields: List) -> str:
        return CreateDepositAccount().Mutate(
            accountName=accountName,
            subfields=subfields
            )

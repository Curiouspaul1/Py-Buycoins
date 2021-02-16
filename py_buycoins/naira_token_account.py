from .gcore.mutations import CreateDepositAccount
from typing import List, Optional
from .exc import InvalidClientObject


class NairaTokenAccount:
    def __init__(self, account_name):
        self.account_name = account_name
    
    def create_account(self, response_fields: List) -> str:
        return CreateDepositAccount().Mutate(
            accountName=self.accountName,
            response_fields=response_fields
            )

    def execute(self, client):
        try:
            return client.execute(query=self.create_account(
                response_fields=[
                    'accountNumber',
                    'accountName',
                    'accountType',
                    'bankName',
                    'accountReference'
                ]
            ))
        except AttributeError:
            raise InvalidClientObject("<BuyCoinsClient> object expected received {} instead".format(type(client)))
    
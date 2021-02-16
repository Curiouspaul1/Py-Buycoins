from .gcore.queries import GetNetworkFee, GetBalance
from .gcore.mutations import SendCoin
from typing import List, Optional
from .exc import SendLimitError, InvalidClientObject


class Send:
    def __init__(self, address: str, cryptocurrency: str, amount: float):
        self.address = address
        self.cryptocurrency = cryptocurrency
        self.amount = amount

    limits = {
        "bitcoin": 1,
        "ethereum": 50,
        "litecoin": 50,
        "nairatoken": 2000000
    }

    def execute(self, client):
        try:
            return client.execute(query=self.send())
        except AttributeError:
            raise InvalidClientObject("<BuyCoinsClient> object expected received {} instead".format(type(client)))

    def get_network_fee(self, response_fields):
        _price = GetNetworkFee()
        return _price.queryObject(
            response_fields=response_fields, 
            cryptocurrency=self.cryptocurrency, amount=self.amount
        )

    def check_limit(self):
        if Send.limits[self.cryptocurrency.lower()] < self.amount:
            return False
        else:
            return True

    def send(self, response_fields):
        if self.cryptocurrency.lower() in Send.limits.keys():
            if self.check_limit(self.amount, self.cryptocurrency):
                return SendCoin().Mutate(
                    cryptocurrency=self.cryptocurrency,
                    response_fields=response_fields,
                    amount=self.amount,
                    address=self.address
                )
            else:
                raise SendLimitError("Maximum daily transaction amount exceeded")

    def balance(self, response_fields: List):
        return GetBalance.queryObject(response_fields=response_fields)

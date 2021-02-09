from gcore.queries import Getnetworkprice, GetBalance
from gcore.mutations import SendCoin
from typing import List, Optional
from exc import SendLimitError


class Send:
    limits = {
        "bitcoin": 1,
        "ethereum": 50,
        "litecoin": 50,
        "nairatoken": 2000000
    }

    def getNetworkFee(self, subfields: List):
        _price = Getnetworkprice()
        return _price.queryObject()

    def check_limit(self, amount, cryptocurrency):
        if Send.limits[cryptocurrency.lower()] < amount:
            return False
        else:
            return True

    def _send(self, amount, cryptocurrency, address, subfields: List):
        if cryptocurrency.lower() in Send.limit.keys():
            if self.check_limit(amount, cryptocurrency):
                return SendCoin(
                    cryptocurrency=cryptocurrency,
                    subfields=subfields,
                    amount=amount,
                    address=address
                ).Mutate()
            else:
                raise SendLimitError("Maximum daily transaction amount exceeded")

    def _balance(self, subfields: List, args: Optional[List[tuple]] = None):
        if args:
            return GetBalance().queryObject(
                _args=args,
                subfields=subfields
            )
        else:
            return GetBalance().queryObject(
                subfields=subfields
            )

from gcore.queries import Getnetworkprice
from gcore.mutations import SendCoin
from typing import List


class Send:
    def getNetworkFee(self, subfields: List):
        _price = Getnetworkprice()
        return _price.queryObject()
    
    def _send(self, amount, cryptocurrency, address, subfields: List):
        return SendCoin(
            cryptocurrency=cryptocurrency,
            subfields=subfields,
            amount=amount,
            address=address
        ).Mutate()

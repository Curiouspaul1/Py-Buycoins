from gcore.queries import Getnetworkprice
from typing import List


class Send:
    def getNetworkFee(self, subfields: List):
        _price = Getnetworkprice()
        return _price.queryObject()
    
    def send(self):
        pass


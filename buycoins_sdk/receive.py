from gcore.mutations import CreateAddress
from typing import List


class Receive:
    def create_address(self, cryptocurrency, subfields: List):
        return createAddress(
            cryptocurrency=cryptocurrency,
            subfields=subfields
        ).Mutate()

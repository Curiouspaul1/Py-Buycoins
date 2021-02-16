from .gcore.mutations import CreateAddress
from typing import List


class Receive:
    def __init__(self, cryptocurrency: str):
        self.cryptocurrency = cryptocurrency
    
    def create_address(self, response_fields: List):
        return CreateAddress().Mutate(
            cryptocurrency=self.cryptocurrency,
            response_fields=response_fields
        )

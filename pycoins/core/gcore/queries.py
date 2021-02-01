from typing import List, Optional


# GraphQL Query
class Query:
    def __init__(self):
        self.name = None

    def queryObject(self, subfields: List, _args: Optional[List[tuple]]=None):
        if _args:
            mod_fields = [f"{i[0]}:{i[1]}" for i in _args]
            _args = tuple(i for i in mod_fields)
            newline = "\n                "
            result = f"""
            query {{
                {self.name}{f"{_args}"}{{
                    {newline.join(i for i in subfields)}
                }}
            }}
            """
            return result.replace("\'", "")
        else:
            newline = "\n                    "
            result = f"""
            query {{
                {self.name}{{
                    {newline.join(i for i in subfields)}
                }}
            }}
            """
            return result


# Get Sale Price
class GetsalePrice(Query):
    """
    Get Sale price for buying
    """
    def __init__(self):
        super().__init__()
        self.name = "getPrices"


class Getnetworkprice(Query):
    """
    Transfer charges
    """
    def __init__(self):
        super().__init__()
        self.name = "getEstimatedNetworkFee"


# getprice = GetsalePrice()
# print(getprice.queryObject(
#     _args=[("id", 1)],
#     subfields=[
#         "id", "cryptocurrency", "buyPricePerCoin"
#     ]
# ))

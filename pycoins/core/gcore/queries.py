from typing import List, Optional


# GraphQL Query
class Query:
    def __init__(self):
        self.name = None

    def queryObject(self, subfields: List, _args: Optional[List[tuple]]=None):
        if _args:
            mod_fields = [f"{i[0]}:\"{i[1]}\"" for i in _args]
            _args = tuple(i.strip("\'") for i in mod_fields)
            newline = "\n"
            result = f"""
            query {{
                {self.name}{_args}{{
                    {newline.join(i for i in subfields)}
                }}
            }}
            """
            return result.replace("\'", "")
        else:
            newline = "\n"
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


# getprice = GetsalePrice()
# print(getprice.queryObject(
#     subfields=[
#         "id", "cryptocurrency", "buyPricePerCoin"
#     ]
# ))
from typing import List, Optional


# GraphQL Base Query
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
class GetSalePrice(Query):
    """
    Get Sale price for buying
    """
    def __init__(self):
        super().__init__()
        self.name = "getPrices"

    def queryObject(self, subfields: Optional[List]=None, cryptocurrency: Optional[str]=None):
        if cryptocurrency:
            if subfields:
                newline = "\n                "
                result = f"""
                query {{
                    {self.name}(cryptocurrency: {cryptocurrency}){{
                        {newline.join(i for i in subfields)}
                    }}
                }}
                """
                return result
            else:
                newline = "\n                "
                result = f"""
                query {{
                    {self.name}(cryptocurrency: {cryptocurrency}){{
                        id
                        status
                        cryptocurrency
                        minBuy
                        minSell
                        maxBuy
                        maxSell
                        minCoinAmount
                        expiresAt
                        buyPricePerCoin
                        sellPricePerCoin
                    }}
                }}
                """
                return result
        else:
            if subfields:
                newline = "\n                    "
                result = f"""
                query {{
                    {self.name}{{
                        {newline.join(i for i in subfields)}
                    }}
                }}
                """
                return result
            else:
                newline = "\n                    "
                result = f"""
                query {{
                    {self.name}{{
                        id
                        status
                        cryptocurrency
                        minBuy
                        minSell
                        maxBuy
                        maxSell
                        minCoinAmount
                        expiresAt
                        buyPricePerCoin
                        sellPricePerCoin
                    }}
                }}
                """
                return result

class GetNetworkFee(Query):
    """
    Transfer charges
    """
    def __init__(self):
        super().__init__()
        self.name = "getEstimatedNetworkFee"


class GetOrders(Query):
    def __init__(self, status):
        super().__init__()
        self.name = "getOrders"
        self.status = status
    
    def queryObject(self, subfields: List):
        newline = "\n                    "
        result = f"""
        query {{
            {self.name}(status: {self.status}){{
                dynamicPriceExpiry
                orders {{
                    edges {{
                        node {{
                            {newline.join(i for i in subfields)}
                        }}
                    }}
                }}
            }}
        }}
        """
        return result


class GetDynamicPriceExpiry(GetOrders):
    """
    Expiration date of a dynamic price
    """
    def __init__(self, status):
        super().__init__()
        self.status = status

    def queryObject(self):
        newline = "\n                    "
        result = f"""
        query {{
            {self.name}(status: {self.status}){{
                dynamicPriceExpiry
        }}
        """
        return result

class GetMarketBook(Query):
    def __init__(self, status):
        super().__init__()
        self.name = "getMarketBook"
        self.status = status
    
    def queryObject(self, subfields: List):
        newline = "\n                       "
        result = f"""
        query {{
            {self.name}(status: {self.status}){{
                dynamicPriceExpiry
                orders {{
                    edges {{
                        node {{
                            {newline.join(i for i in subfields)}
                        }}
                    }}
                }}
            }}
        }}
        """
        return result


class GetBalance(Query):
    def __init__(self):
        super().__init__()
        self.name = "getBalance"
    

# getprice = GetsalePrice()
# print(getprice.queryObject())

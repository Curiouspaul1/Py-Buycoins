from typing import List, Optional


# GraphQL Base Query
class Query:
    def __init__(self):
        self.name = None

    def queryObject(self, response_fields: List, fields: Optional[List[tuple]]=None):
        if fields:
            mod_fields = [f"{i[0]}:{i[1]}" for i in fields]
            fields = tuple(i for i in mod_fields)
            newline = "\n                "
            result = f"""
            query {{
                {self.name}{f"{fields}"}{{
                    {newline.join(i for i in response_fields)}
                }}
            }}
            """
            return result.replace("\'", "")
        else:
            newline = "\n                    "
            result = f"""
            query {{
                {self.name}{{
                    {newline.join(i for i in response_fields)}
                }}
            }}
            """
            return result


# Get Sale Price
class BuyCoinsPrices(Query):
    """
    Buycoins prices
    """
    def __init__(self):
        super().__init__()
        self.name = "buycoinsPrices"


    def queryObject(self, side: str, mode: str, cryptocurrency: str, response_fields: List):
        newline = "\n                    "
        result = f"""
        query {{
            {self.name}(side: {side}, mode: {mode}, cryptocurrency: {cryptocurrency}){{
                {newline.join(i for i in response_fields)}
            }}
        }}
        """
        return result


class GetPrices(Query):
    def __init__(self):
        super().__init__()
        self.name = 'getPrices'

    def queryObject(self, response_fields: List, cryptocurrency: Optional[str]=None):
        if cryptocurrency:
            newline = "\n                    "
            result = f"""
            query {{
                {self.name} (cryptocurrency: {cryptocurrency}){{
                    {newline.join(i for i in response_fields)}
                }}
            }}
            """
            return result
        else:
            newline = "\n                    "
            result = f"""
            query {{
                {self.name}{{
                    {newline.join(i for i in response_fields)}
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
    
    def queryObject(self, cryptocurrency: str, amount: float, response_fields: List):
        newline = "\n                    "
        result = f"""
        query {{
            {self.name}(cryptocurrency: {cryptocurrency}, amount: {amount}) {{
                {newline.join(i for i in response_fields)}
            }}
        }}
        """
        return result


class GetOrders(Query):
    def __init__(self):
        super().__init__()
        self.name = "getOrders"
    
    def queryObject(self, status, response_fields: List):
        newline = "\n                    "
        result = f"""
        query {{
            {self.name}(status: {self.status}){{
                dynamicPriceExpiry
                orders {{
                    edges {{
                        node {{
                            {newline.join(i for i in response_fields)}
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
    def __init__(self):
        self.name = 'getOrders'

    def queryObject(self, status):
        newline = "\n                    "
        result = f"""
        query {{
            {self.name}(status: {self.status}){{
                dynamicPriceExpiry
        }}
        """
        return result


class GetMarketBook(Query):
    def __init__(self):
        self.name = "getMarketBook"
    
    def queryObject(self, response_fields: List):
        newline = "\n                       "
        result = f"""
        query {{
            {self.name}{{
                dynamicPriceExpiry
                orders {{
                    edges {{
                        node {{
                            {newline.join(i for i in response_fields)}
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
        self.name = "getBalances"

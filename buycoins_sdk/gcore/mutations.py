from typing import List, Optional


class Mutation:
    """
    Pls Add a description
    """
    def __init__(self):
        self.name = None

    def Mutate(self, fields: List[tuple], response_fields: List):
        mod_fields = [f"{i[0]}: {str(i[1])}" for i in fields]
        _args = tuple(i.strip("\'") for i in mod_fields)
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}{_args} {{
                {newline.join(i for i in response_fields)}
            }}
        }}
        """
        return result.replace("\'", "")


class CreateDepositAccount(Mutation):
    def __init__(self):
        """
        Create deposit account
        """
        self.name = "createDepositAccount"
    
    def Mutate(self, accountName: str, response_fields: List):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(accountName: \"{f"{accountName}"}\") {{
                {newline.join(i for i in response_fields)}
            }}
        }}
        """
        return result


# Buy from BuyCoins
class Buy(Mutation):
    def __init__(self):
        """
        Buy crypto
        """
        super().__init__()
        self.name = "buy"

    def Mutate(self, price: str, coin_amount: float, cryptocurrency, response_fields: List):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(price: \"{f"{price}"}\", coin_amount: {coin_amount}, cryptocurrency: {cryptocurrency})
            {{
                {newline.join(i for i in response_fields)}
            }}
        }}
        """
        return result


class PostLimitOrder(Mutation):
    def __init__(self):
        super().__init__()
        self.name = "postLimitOrder"
        
    def Mutate(self, order_side: str, coin_amount: float, cryptocurrency: str, price_type: str, response_fields: List, static_price=None, dynamic_exchange_rate=None):
        newline = "\n                "
        if price_type == 'static':
            result = f"""
            mutation {{
                {self.name}(orderSide: {order_side}, coinAmount: {coin_amount}, cryptocurrency: {cryptocurrency}, staticPrice: {static_price}, priceType: {price_type})
                {{
                    {newline.join(i for i in response_fields)}
                }}
            }}
            """
        elif price_type == 'dynamic':
            result = f"""
            mutation {{
                {self.name}(orderSide: {order_side}, coinAmount: {coin_amount}, cryptocurrency: {cryptocurrency}, dynamicExchangeRate: {dynamic_exchange_rate}, priceType: {price_type})
                {{
                    {newline.join(i for i in response_fields)}
                }}
            }}
            """
        return result

    
class PostMarketOrder(Mutation):
    def __init__(self):
        super().__init__()
        self.name = "postMarketOrder"


    def Mutate(self, order_side: str, coin_amount: float, cryptocurrency: str, response_fields: List):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(orderSide: {order_side}, coinAmount: {coin_amount}, cryptocurrency: {cryptocurrency})
            {{
                {newline.join(i for i in response_fields)}
            }}
        }}
        """
        return result


class Sell(Mutation):
    def __init__(self):
        """
        Sell crypto
        """
        super().__init__()
        self.name = "sell"


    def Mutate(self, response_fields: List, price: str, coin_amount: float, cryptocurrency):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(price: \"{f"{price}"}\", coin_amount: {coin_amount}, cryptocurrency: {cryptocurrency})
            {{
                {newline.join(i for i in response_fields)}
            }}
        }}
        """
        return result


class SendCoin(Mutation):
    def __init__(self):
        super().__init__()
        self.name = "send"

    def Mutate(self, cryptocurrency, address, amount, response_fields: List):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(cryptocurrency: {cryptocurrency}, amount: {amount}, address: \"{f"{address}"}\")
            {{
                {newline.join(i for i in response_fields)}
                transaction {{
                    hash
                    id
                }}
            }}
        }}
        """
        return result


class CreateAddress(Mutation):
    def __init__(self):
        super().__init__()
        self.name = "createAddress"

    def Mutate(self, cryptocurrency, response_fields: List):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(cryptocurrency: {cryptocurrency})
            {{
                {newline.join(i for i in response_fields)}
            }}
        }}
        """
        return result

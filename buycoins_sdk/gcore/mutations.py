from typing import List, Optional


class Mutation:
    """
    Pls Add a description
    """
    def __init__(self):
        self.name = None

    def Mutate(self, fields: List[tuple], subfields: List):
        mod_fields = [f"{i[0]}: {str(i[1])}" for i in fields]
        _args = tuple(i.strip("\'") for i in mod_fields)
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}{_args} {{
                {newline.join(i for i in subfields)}
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
    
    def Mutate(self, accountName: str, subfields: List):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(accountName: \"{f"{accountName}"}\") {{
                {newline.join(i for i in subfields)}
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

    def Mutate(self, price: str, coin_amount: float, cryptocurrency, subfields: Optional[List]=None):
        if subfields:
            newline = "\n                "
            result = f"""
            mutation {{
                {self.name}(price: \"{f"{price}"}\", coin_amount: {coin_amount}, cryptocurrency: {cryptocurrency})
                {{
                    {newline.join(i for i in subfields)}
                }}
            }}
            """
            return result
        else:
            newline = "\n                "
            result = f"""
            mutation {{
                {self.name}(price: \"{f"{price}"}\", coin_amount: {coin_amount}, cryptocurrency: {cryptocurrency})
                {{
                    id
                    price {{
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
                    cryptocurrency
                    filledCoinAmount
                    side
                    status
                    totalCoinAmount
                    createdAt
                }}
            }}
            """
            return result


class PostLimitOrder(Mutation):
    def __init__(self):
        super().__init__()
        self.name = "postLimitOrder"
        
    def Mutate(self, order_side: str, coin_amount: float, cryptocurrency: str, price_type: str, subfields: List, static_price=None, dynamic_exchange_rate=None):
        newline = "\n                "
        if price_type == 'static':
            result = f"""
            mutation {{
                {self.name}(orderSide: {order_side}, coinAmount: {coin_amount}, cryptocurrency: {cryptocurrency}, staticPrice: {static_price}, priceType: {price_type})
                {{
                    {newline.join(i for i in subfields)}
                }}
            }}
            """
        elif price_type == 'dynamic':
            result = f"""
            mutation {{
                {self.name}(orderSide: {order_side}, coinAmount: {coin_amount}, cryptocurrency: {cryptocurrency}, dynamicExchangeRate: {dynamic_exchange_rate}, priceType: {price_type})
                {{
                    {newline.join(i for i in subfields)}
                }}
            }}
            """
        return result

    
class PostMarketOrder(Mutation):
    def __init__(self):
        super().__init__()
        self.name = "postMarketOrder"


    def Mutate(self, order_side: str, coin_amount: float, cryptocurrency: str, subfields: List):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(orderSide: {order_side}, coinAmount: {coin_amount}, cryptocurrency: {cryptocurrency})
            {{
                {newline.join(i for i in subfields)}
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


    def Mutate(self, subfields: List, price: str, coin_amount: float, cryptocurrency):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(price: \"{f"{price}"}\", coin_amount: {coin_amount}, cryptocurrency: {cryptocurrency})
            {{
                {newline.join(i for i in subfields)}
            }}
        }}
        """
        return result


class SendCoin(Mutation):
    def __init__(self):
        super().__init__()
        self.name = "send"

    def Mutate(self, cryptocurrency, address, amount, subfields: List):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(cryptocurrency: {cryptocurrency}, amount: {amount}, address: \"{f"{address}"}\")
            {{
                {newline.join(i for i in subfields)}
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

    def Mutate(self, cryptocurrency, subfields: List):
        newline = "\n                "
        result = f"""
        mutation {{
            {self.name}(cryptocurrency: {cryptocurrency})
            {{
                {newline.join(i for i in subfields)}
            }}
        }}
        """
        return result

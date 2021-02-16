from typing import List, Optional


class Mutation:
    """
    The Mutation class is the parent class for all sub-mutation classes in the library.
    """
    def __init__(self):
        self.name = None

    def Mutate(self, fields: List[tuple], response_fields: List):
        """
        Automatically and crudely generates mutation queries on behalf of user.
        Should be used in place of the other subclasses, if user wishes to customize his/her
        queries completely from scratch.

        Args:
            fields (List[tuple]): A list of tuples with length of two(2).
            The first item (tuple[0]) in each tuple corresponds or should correspond to the name of a field to be specified
            as a mutation argument/field. The second item in each tuple (tuple[1]), corresponds to
            the value of tuple[0]. This would be such that:

                fields = [('name','Josh'),('age',14)]
            would correspond to:
                mutation{
                    createUser(name: 'Josh', age: 14){
                        response_fields
                    }
                }
            
            response_fields (List): A list of string values that correspond to the names of,
            response fields, that a user wants to be returned or specified in the response from
            the GraphQL API. Typically:
                subfields = ['id', 'name']
            would correspond to:
                mutation{
                    createUser(name: 'Josh', age: 14){
                        id,
                        name
                    }
                }
        """
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
        Create deposit account mutation class inherits from <class 'Mutation'>
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
        Buy crypto (from buycoins) mutation class inherits from <class 'Mutation'>
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
    """
    Post limit order mutation class inherits from <class 'Mutation'>
    """
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
    """
        Create deposit account mutation class inherits from <class 'Mutation'>
    """
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
            Sell crypto mutation class inherits from <class 'Mutation'>
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
    """
        Send crypto mutation class inherits from <class 'Mutation'>
    """
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
    """
        Create address mutation class inherits from <class 'Mutation'>
    """
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

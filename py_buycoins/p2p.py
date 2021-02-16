from .gcore.mutations import Buy, PostLimitOrder, PostMarketOrder
from .gcore.queries import GetOrders, GetMarketBook, GetDynamicPriceExpiry, BuyCoinsPrices
from typing import List, Optional
from .exc import InvalidClientObject


# P2P purchase
class BuyCoinsP2P:
    def __init__(
        self,
        order_side: str,
        coin_amount: float,
        cryptocurrency: str,
        price_type: str,
        status: str,
        static_price=None,
        dynamic_exchange_rate=None
    ):
        self.order_side = order_side
        self.coin_amount = coin_amount
        self.cryptocurrency = cryptocurrency
        self.price_type = price_type
        self.static_price = static_price
        self.dynamic_exchange_rate = dynamic_exchange_rate
        self.status = status

    def get_dynamic_price(self) -> str:
        return GetDynamicPriceExpiry().queryObject(
            status=self.status
        )

    def get_orders(self, response_fields: List) -> str:
        return GetOrders().queryObject(
            status=self.status,
            response_fields=response_fields
        )

    def get_market_book(self, response_fields: List) -> str:
        return GetMarketBook().queryObject(
            response_fields=response_fields
        )

    def post_limit_order(self, response_fields: List):
        return PostLimitOrder().Mutate(
            order_side=self.order_side,
            coin_amount=self.coin_amount,
            cryptocurrency=self.cryptocurrency,
            price_type=self.price_type,
            static_price=self.static_price,
            dynamic_exchange_rate=self.dynamic_exchange_rate,
            response_fields=response_fields
        )

    def post_market_order(self, response_fields: List):
        return PostMarketOrder().Mutate(
            order_side=self.order_side,
            coin_amount=self.coin_amount,
            cryptocurrency=self.cryptocurrency,
            response_fields=response_fields
        )

    def execute(self, client, limit_order=None):
        if limit_order:
            try:
                return client.execute(query=self.post_limit_order(response_fields=[
                    'id', 'minCoinAmount', 'cryptocurrency',
                    'maxBuy', 'status', 'minBuy', 'mode',
                    'minSell', 'maxSell', 'mode'
                    'buyPricePerCoin', 'sellPricePerCoin'
                ]))
            except AttributeError:
                raise InvalidClientObject("<BuyCoinsClient> object expected received {} instead".format(type(client)))
        else:
            try:
                return client.execute(query=self.post_market_order(response_fields=[
                    'id', 'coinAmount', 'cryptocurrency',
                    'side', 'status', 'createdAt',
                    'pricePerCoin', 'priceType',
                    'dynamicExchangeRate', 'staticPrice'
                ]))
            except AttributeError:
                raise InvalidClientObject("<BuyCoinsClient> object expected received {} instead".format(type(client)))
    
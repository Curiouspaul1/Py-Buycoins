from gcore.mutations import Buy, PostLimitOrder, PostMarketOrder
from gcore.queries import GetOrders, GetMarketBook, GetDynamicPriceExpiry, BuyCoinsPrices
from typing import List, Optional


# P2P purchase
class BuyCoinsP2P():    
    # This query type doesn't exist on BuyCoins server but it's specified in the documentation
    # def get_buycoins_prices(self, side: str, mode: str, cryptocurrency: str, subfields: List) -> str:
    #    return BuyCoinsPrices().queryObject(
    #        side=side,
    #        mode=mode,
    #        cryptocurrency=cryptocurrency,
    #        subfields=subfields
    #    )

    def get_dynamic_price(self, status: str) -> str:
        return GetDynamicPriceExpiry().queryObject(
            status=status
        )

    def get_orders(self, status: str, subfields: List) -> str:
        return GetOrders().queryObject(
            status=status,
            subfields=subfields
        )

    def get_market_book(self, subfields: List) -> str:
        return GetMarketBook().queryObject(
            subfields=subfields
        )

    def post_limit_order(self, order_side: str, coin_amount: float, cryptocurrency: str, price_type: str, subfields: List, static_price=None, dynamic_exchange_rate=None):
        return PostLimitOrder().Mutate(
            order_side=order_side,
            coin_amount=coin_amount,
            cryptocurrency=cryptocurrency,
            price_type=price_type,
            static_price=static_price,
            dynamic_exchange_rate=dynamic_exchange_rate,
            subfields=subfields
        )

    def post_market_order(self, order_side: str, coin_amount: float, cryptocurrency: str, subfields: List):
        return PostMarketOrder().Mutate(
            order_side=order_side,
            coin_amount=coin_amount,
            cryptocurrency=cryptocurrency,
            subfields=subfields
        )

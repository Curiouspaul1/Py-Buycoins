from gcore.mutations import Buy, PostLimitOrder, PostMarketOrder
from gcore.queries import GetOrders, GetMarketBook, GetDynamicPriceExpiry
from typing import List, Optional


# P2P purchase
class BuycoinsP2P():
    def __init__(self):
        super().__init__()
    
    def get_dynamic_price(self, status: str) -> str:
        return GetDynamicPriceExpiry(
            status=status
        ).queryObject()

    def get_orders(self, status: str, subfields: List) -> str:
        return GetOrders(
            status=status
        ).queryObject(subfields=subfields)

    def get_market_book(self, status: str, subfields: List) -> str:
        return GetMarketBook(
            status=status
        ).queryObject(subfields=subfields)

    def limit_order(self, subfields: List, order_side: str, coin_amount: float, cryptocurrency, price_type: str, price_type_value: Optional[List[tuple]]=None):
        order = PostLimitOrder(
            subfields=subfields,
            order_side=order_side,
            coin_amount=coin_amount,
            cryptocurrency=cryptocurrency,
            price_type=price_type,
            price_type_value=price_type_value
        )
        return order.Mutate()

    def market_order(self, subfields: List, order_side: str, coin_amount: float, cryptocurrency: str):
        order = PostMarketOrder(
            subfields=subfields,
            order_side=order_side,
            coin_amount=coin_amount,
            cryptocurrency=cryptocurrency
        )
        return order.Mutate()
        
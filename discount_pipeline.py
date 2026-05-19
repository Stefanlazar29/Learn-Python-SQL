from abc import  ABC, abstractmethod

from huggingface_hub.cli.cache import print_cache_entries_json


#Contract for any tip of discount
class DiscountStrategy(ABC):
    @abstractmethod
    def apply (self, price: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply (self, price: float) -> float:
        return price

class SeasonalDiscount(DiscountStrategy):
    def apply (self, price: float) -> float:
        return price * 0.9 #discount -10%

class VIPDiscount(DiscountStrategy):
    def apply (self, price: float) -> float:
        return price * 0.8 #discount -20%


#The context that`s using the strategy
class Order:
    def __init__ (self, price: float, discount: DiscountStrategy):
        self.price = price
        self.discount = discount

    def get_total (self) -> float:
        return self.discount.apply(self.price)

#PROCESSING
order_1 = Order(100.0, SeasonalDiscount())
order_2 = Order(100.0, VIPDiscount())

print(f"Total sezonal: {order_1.get_total()}")
print(f"Total VIP: {order_2.get_total()}")

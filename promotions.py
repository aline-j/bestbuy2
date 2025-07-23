from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Applies promotion and returns discounted price
        """
        pass


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return total_price - discount


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        price_per_unit = product.price
        num_half_price = quantity // 2
        num_full_price = quantity - num_half_price
        total_cost = num_full_price * price_per_unit + num_half_price * price_per_unit * 0.5
        return total_cost


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        number_of_free_items = quantity // 3
        number_of_paid_items = quantity - number_of_free_items
        total_price = number_of_paid_items * product.price
        return total_price

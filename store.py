from typing import List, Tuple
from products import Product


class Store:
    """
    Represents a store that manages a collection of products.
    Provides methods for adding, removing, listing, and ordering products.
    """

    def __init__(self, products: List[Product]):
        """
        Initializes the store with a list of products.

        :param products: List of Product instances to initialize the store with.
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Adds a product to the store's inventory.

        :param product: Product to add.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store's inventory.

        :param product: Product to remove.
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all active products in the store.

        :return: Total quantity of all active products.
        """
        total_quantity = 0
        for product in self.products:
            if product.is_active():
                total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """
        Returns a list of all active products in the store.

        :return: List of active Product instances.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    @staticmethod
    def order(shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order based on a list of (product, quantity) tuples.

        :param shopping_list: List of tuples with products and desired quantities.
        :return: Total price of the processed order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

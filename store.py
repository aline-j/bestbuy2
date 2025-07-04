from typing import List, Tuple
import products


class Store:
    """
    Represents a store that manages a collection of products.
    Provides methods for adding, removing, listing, and ordering products.
    """

    def __init__(self, products: List[products.Product]):
        """
        Initializes the store with a list of products.

        :param products: List of Product instances to initialize the store with.
        """
        self.products = products

    def add_product(self, product: products.Product):
        """
        Adds a product to the store's inventory.

        :param product: Product to add.
        """
        self.products.append(product)

    def remove_product(self, product: products.Product):
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

    def get_all_products(self) -> List[products.Product]:
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
    def order(shopping_list: List[Tuple[products.Product, int]]) -> float:
        """
        Processes an order based on a list of (product, quantity) tuples.

        :param shopping_list: List of tuples with products and desired quantities.
        :return: Total price of the processed order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()

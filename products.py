class Product:
    """
    A class representing a product in an inventory system.

    Attributes:
        name (str): The name of the product.
        price (float): The price of a single unit.
        quantity (int): Available stock.
        active (bool): Status of the product (True if available for sale).
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new Product instance.

        Raises:
            ValueError: If name is empty, or price/quantity is negative.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def get_quantity(self) -> int:
        """
        Returns the current quantity in stock.

        Returns:
            int: The quantity available.
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Updates the quantity. If it reaches 0, the product is deactivated.

        Args:
            quantity (int): New quantity value.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks whether the product is active.

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self) -> None:
        """
        Activates the product (sets active to True).
        """
        self.active = True

    def deactivate(self) -> None:
        """
        Deactivates the product (sets active to False).
        """
        self.active = False

    def show(self) -> None:
        """
        Prints a human-readable summary of the product.
        """
        if self.promotion:
            promo = f", Promotion: {self.promotion.name}"
        else:
            promo = ", Promotion: None"

        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promo}")

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase of the given quantity.

        Args:
            quantity (int): Amount to purchase.

        Returns:
            str: The total cost as a string with € symbol.

        Raises:
            ValueError: If product is inactive, quantity is invalid,
                        or not enough stock is available.
        """
        if not self.active:
            raise ValueError("Cannot buy an inactive product.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")

        # Apply promotion (if available)
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    """
    A non-stocked product (e.g., Microsoft Windows license).
    Always has quantity 0 and cannot be updated.
    """
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int) -> None:
        """
        Override the set_quantity method to prevent updating.
        Args:
            quantity:
        """
        pass    # Ignore quantity changes

    def get_quantity(self) -> int:
        return 0

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise ValueError("Cannot buy an inactive product.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        # No quantity check needed
        return quantity * self.price

    def show(self):
        if self.promotion:
            promo = f", Promotion: {self.promotion.name}"
        else:
            promo = ", Promotion: None"

        print(f"{self.name}, Price: ${self.price}{promo}")


class LimitedProduct(Product):
    """
    A product with a purchase limit per order.
    """
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} items per order.")
        return super().buy(quantity)

    def show(self):
        if self.promotion:
            promo = f", Promotion: {self.promotion.name}"
        else:
            promo = ", Promotion: None"

        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promo}")

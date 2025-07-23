import pytest
from products import Product


def test_create_valid_product():
    # Test that creating a normal product works.
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() == True


def test_create_product_with_empty_name():
    # Test that creating a product with an empty name invokes an exception.
    with pytest.raises(ValueError, match="Product name cannot be empty."):
        Product("", price=1450, quantity=100)


def test_create_product_with_negative_price():
    # Test that creating a product with a negative price invokes an exception.
    with pytest.raises(ValueError, match="Product price cannot be negative."):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_quantity_zero_becomes_inactive():
    # Test that when a product reaches 0 quantity, it becomes inactive.
    product = Product("Bose Headphones", price=250, quantity=1)
    product.buy(1)
    assert product.get_quantity() == 0
    assert product.is_active() == False


def test_product_purchase_modifies_quantity_and_returns_total_price():
    # Test that product purchase modifies the quantity and returns the right output.
    product = Product("Pixel 7", price=500, quantity=10)
    total = product.buy(3)
    assert total == 1500
    assert product.get_quantity() == 7


def test_buying_more_than_stock():
    # Test that buying a larger quantity than exists invokes exception.
    product = Product("Logitech Mouse", price=50, quantity=5)
    with pytest.raises(ValueError, match="Not enough quantity in stock."):
        product.buy(10)

import pytest
from products import Product
from store import Store


@pytest.fixture
def sample_products():
    return [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250,
                quantity=0),  # Inactive by default
        Product("Google Pixel 7", price=500, quantity=50),
    ]


@pytest.fixture
def store_with_products(sample_products):
    return Store(sample_products)


def test_add_product(store_with_products):
    new_product = Product("iPad Pro", price=1200, quantity=30)
    store_with_products.add_product(new_product)
    assert new_product in store_with_products.products


def test_remove_product(store_with_products):
    product_to_remove = store_with_products.products[0]
    store_with_products.remove_product(product_to_remove)
    assert product_to_remove not in store_with_products.products


def test_get_total_quantity(store_with_products):
    total = store_with_products.get_total_quantity()
    # Only active products: MacBook (100) and Pixel (50), not Bose (0)
    assert total == 150


def test_get_all_products_returns_only_active(store_with_products):
    active_products = store_with_products.get_all_products()
    assert all(p.is_active() for p in active_products)
    assert len(active_products) == 3  # Only MacBook and Pixel


def test_order_process_reduces_quantities_and_returns_total(
        store_with_products):
    macbook = store_with_products.products[0]
    pixel = store_with_products.products[2]

    order = [(macbook, 2), (pixel, 3)]  # 2x1450 + 3x500 = 2900 + 1500 = 4400
    total_price = store_with_products.order(order)

    assert total_price == 4400
    assert macbook.get_quantity() == 98
    assert pixel.get_quantity() == 47


def test_order_raises_error_for_invalid_quantity(store_with_products):
    pixel = store_with_products.products[2]
    with pytest.raises(ValueError, match="Not enough quantity in stock."):
        store_with_products.order([(pixel, 999)])

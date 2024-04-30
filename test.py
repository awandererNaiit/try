import pytest
from main import BaseProduct, Product, Category, Smartphone, LawnGrass


def test_new_product_with_zero_quantity():
    with pytest.raises(ValueError):
        Product.new_product({'name': 'Товар', 'description': 'Описание', 'price': 100, 'quantity': 0})


def test_calculate_average_price_with_no_products():
    category = Category()
    assert category.calculate_average_price() == 0


@pytest.mark.parametrize("products, expected_average_price", [
    ([Product('Товар 1', 'Описание', 100, 5), Product('Товар 2', 'Описание', 50, 3)], 75.0),
])
def test_calculate_average_price_with_products(products, expected_average_price):
    category = Category()
    category.products = products
    assert category.calculate_average_price() == expected_average_price

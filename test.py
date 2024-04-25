import pytest

from main import Category, Product


class TestCategory:
    def test_create_category(self):
        category = Category('категория', 'Описание категории')
        assert category.name == 'категория'
        assert category.description == 'Описание категории'

    def test_add_product(self):
        category = Category('категория', 'Описание категории')
        product = Product.create_product('продукт', 'Описание продукта', 100500, 10)
        category.add_product(product)
        assert len(category.products) == 1
        assert Category.total_unique_products == 1

    def test_remove_product(self):
        category = Category('категория', 'Описание категории')
        product = Product.create_product('продукт', 'Описание продукта', 100500, 10)
        category.add_product(product)
        category.remove_product(product)
        assert len(category.products) == 0
        assert Category.total_unique_products == 0

    def test_get_products_info(self):
        category = Category('категория', 'Описание категории')
        product1 = Product.create_product('продукт 1', 'Описание продукта 1', 100500, 10)
        product2 = Product.create_product('продукт 2', 'Описание продукта 2', 200, 5)
        category.add_product(product1)
        category.add_product(product2)
        products_info = category.get_products_info()
        assert products_info == [
            'продукт 1, 100500 руб. Остаток: 10 шт.',
            'продукт 2, 200 руб. Остаток: 5 шт.',
        ]


class TestProduct:
    def test_create_product(self):
        product = Product.create_product('продукт', 'Описание продукта', 100500, 10)
        assert product.name == 'продукт'
        assert product.description == 'Описание продукта'
        assert product.price == 100500
        assert product.amount == 10

    def test_set_price(self):
        product = Product.create_product('продукт', 'Описание продукта', 100500, 10)
        product.price = 200
        assert product.price == 200

        product.price = -50
        assert product.price == 200
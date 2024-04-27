import pytest
from main import Product, Smartphone, LawnGrass, ProductCreationMixin

class TestProduct:
    def test_product_is_abstract(self):
        with pytest.raises(TypeError):
            Product()

    def test_smartphone_specific_info(self):
        # Передаем все необходимые аргументы для создания объекта Smartphone
        smartphone = Smartphone('Apple', 'iPhone', '12 Pro', '256GB', 'Silver', 'iOS', 6.1, 'Silver')
        assert smartphone.specific_info() == "Operating System: iOS, Screen Size: 6.1 inches"

    def test_lawngrass_specific_info(self):
        lawngrass = LawnGrass('Bermuda', 'Hybrid', 'Green', 'Full Sun')
        assert lawngrass.specific_info() == "Type: Hybrid, Color: Green, Sunlight: Full Sun"

class TestProductCreationMixin:
    def test_creation_mixin(self, capsys):
        class TestClass(ProductCreationMixin):
            def __init__(self, name):
                self.name = name

        test_object = TestClass('Test')
        test_object.specific_info()  # Вызываем метод specific_info() для логирования
        captured = capsys.readouterr()
        assert captured.out == "Object Test created.\n"
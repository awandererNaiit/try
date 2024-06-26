from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def new_product(self, *args):
        pass


class PrintMixin:

    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"создан объект со свойствами {object_attributes})"


class Product(BaseProduct, PrintMixin):
    """
    Класс для описания товара в магазине
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n'

    @classmethod
    def new_product(cls, product_data: dict):
        if product_data.get('quantity', 0) == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        return cls(**product_data)

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price

    @property
    def amount(self):
        return self._amount

    @name.setter
    def name(self, value):
        self._name = value

    @description.setter
    def description(self, value):
        self._description = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', price={self.price}, amount={self.amount})"


class Category:
    def __init__(self):
        self.products = []

    def __len__(self):
        return len(self.products)

    def add_product(self, product):
        if product.quantity == 0:
            raise ValueError("Нельзя добавить товар с нулевым количеством!")
        self.products.append(product)

    def calculate_average_price(self):
        total_price = 0
        total_products = len(self.products)
        if total_products == 0:
            return 0
        try:
            for product in self.products:
                total_price += product.price
            average_price = total_price / total_products
            return average_price
        except ZeroDivisionError:
            return 0


class Smartphone(Product):
    def __init__(self, name, description, price, amount, brand, model, storage, color):
        super().__init__(name, description, price, amount)
        self._brand = brand
        self._model = model
        self._storage = storage
        self._color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, amount, origin, duration, color):
        super().__init__(name, description, price, amount)
        self._origin = origin
        self._duration = duration
        self._color = color

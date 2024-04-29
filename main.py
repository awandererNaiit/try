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

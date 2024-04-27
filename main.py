from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def new_product(self, *args):
        pass


class ProductCreationMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        object_attributes = ', '.join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"создан объект со свойствами: {object_attributes}"


class Smartphone(BaseProduct, ProductCreationMixin):
    def __init__(self, name, description, price, amount, brand, model, storage, color):
        super().__init__()
        self._name = name
        self._description = description
        self._price = price
        self._amount = amount
        self._brand = brand
        self._model = model
        self._storage = storage
        self._color = color

    def specific_info(self):
        return f"Brand: {self._brand}, Model: {self._model}, Storage: {self._storage}, Color: {self._color}"

    def new_product(self, *args):
        return Smartphone(*args)


class LawnGrass(BaseProduct, ProductCreationMixin):
    def __init__(self, name, description, price, amount, origin, duration, color):
        super().__init__()
        self._name = name
        self._description = description
        self._price = price
        self._amount = amount
        self._origin = origin
        self._duration = duration
        self._color = color

    def specific_info(self):
        return f"Origin: {self._origin}, Duration: {self._duration}, Color: {self._color}"

    def new_product(self, *args):
        return LawnGrass(*args)
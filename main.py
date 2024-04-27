from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name, description, price, amount):
        self._name = name
        self._description = description
        self._price = price
        self._amount = amount

    @abstractmethod
    def specific_info(self):
        pass

    @abstractmethod
    def new_product(self, *args):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', '{self._description}', {self._price}, {self._amount})"

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

    @price.setter
    def price(self, value):
        self._price = value

    @amount.setter
    def amount(self, value):
        self._amount = value


class ProductCreationMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        object_attributes = ', '.join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"создан объект со свойствами: {object_attributes}"


class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self._products = []
        Category.total_categories += 1

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products

    def add_product(self, product):
        if not isinstance(product, BaseProduct):
            raise TypeError("Нельзя добавлять разные продукты")
        self._products.append(product)
        Category.total_unique_products += 1

    def remove_product(self, product):
        self._products.remove(product)
        Category.total_unique_products -= 1

    def get_products_info(self):
        products_info = []
        for product in self._products:
            product_info = f"{product.name}, {product.price} руб. Остаток: {product.amount} шт."
            products_info.append(product_info)
        return products_info

    def __str__(self):
        total_products = len(self)
        return f"{self.name}, количество продуктов: {total_products} шт."

    def __len__(self):
        return sum(product.amount for product in self._products)


class Smartphone(BaseProduct, ProductCreationMixin):
    def __init__(self, name, description, price, amount, brand, model, storage, color):
        super().__init__(name, description, price, amount)
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
        super().__init__(name, description, price, amount)
        self._origin = origin
        self._duration = duration
        self._color = color

    def specific_info(self):
        return f"Origin: {self._origin}, Duration: {self._duration}, Color: {self._color}"

    def new_product(self, *args):
        return LawnGrass(*args)
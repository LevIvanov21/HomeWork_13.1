from src.abstract_product import AbstractProduct
from src.Mixinlog import Mixinlog


class Category:
    """Создадим класс "Категории" для вывода товара, его описания"""
    all_quantity_category = 0
    all_quantity_unique_product = 0
    name: str
    description: str
    __product: list

    def __init__(self, name: str, description: str, product: list):
        self.name = name
        self.description = description
        self.__product = product
        self.all_quantity_category = 1
        Category.all_quantity_unique_product += 1
        self.all_quantity_category = Category.all_quantity_category
        self.all_quantity_unique_product = Category.all_quantity_unique_product

    def __str__(self):
        return f"{self.__class__.__name__}\nКоличество продуктов: {len(self)}"

    def __len__(self):
        product_len = 0
        for i in self.__product:
            product_len += i.quantity_in_stock
        return product_len

    def add_product(self, value):
        """метод, который будет принимать на вход объект товара и добавлять его в список."""
        if isinstance(value, Product):
            if value.quantity_in_stock == 0:
                raise TypeError("Невозможно добавить любой другой объект")
            self.__product.append(value)
        raise ValueError("Нельзя добавить товар с нулевым количеством.")

    @property
    def product(self):
        """декоратор для вывода товара в формате"""
        output = " "
        for product in self.__product:
            output += f"{product.name}\n{float(product.price)} шт.\nВ наличии{product.quantity_in_stock} "
        return output

    def average(self):
        """
       Функия для поиски среднего ценника всех продуктов
       """
        product_sum = 0
        try:
            for product in self.__product:
                product_sum += product.price
            result = product_sum / len(self.__product)
            return result
        except ZeroDivisionError:
            return 0


class Product(AbstractProduct, Mixinlog):
    """Саздадим класс "Продукт" для развертывания информации о товаре"""
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int):
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity_in_stock = quantity_in_stock

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock):
        return cls(name, description, price, quantity_in_stock)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price >= 550000:
            self.__price = new_price
        else:
            print("Введена некорректная сумма")

    def __str__(self):
        return f"{self.__class__.__name__}, {self.price} руб.\nОстаток: {self.quantity_in_stock} шт."

    def __add__(self, other):
        if self.quantity_in_stock == 0 or other.quantity_in_stock == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
        if type(other) == type(self):
            return self.price * self.quantity_in_stock + other.price * other.quantity_in_stock
        else:
            raise TypeError("Можно складывать товары только из одинаковых классов продуктов.")


class Smartphone(Product):
    """Класс наследуется от базового класса Product c добавлением следующих свойств:
    производительность, модель, объем встроенной памяти, цвет."""
    performance: int
    model: str
    built_in_memory: int
    color: str

    def __init__(self, performance: int, model: str, built_in_memory: int, color: str,
                 name: str, description: str, price: float,
                 quantity_in_stock: int):
        super().__init__(name, description, price, quantity_in_stock)
        self.performance = performance
        self.model = model
        self.built_in_memory = built_in_memory
        self.color = color


class LawnGrass(Product):
    """Класс наследуется от базового класса Product c добавлением следующих свойств:
    страна-производитель, срок прорастания, цвет."""
    manufacturer_country: str
    germination_period: int
    color: str

    def __init__(self, manufacturer_country: str, germination_period: int, color: str, name: str, description: str,
                 price: float,
                 quantity_in_stock: int):
        super().__init__(name, description, price, quantity_in_stock)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color
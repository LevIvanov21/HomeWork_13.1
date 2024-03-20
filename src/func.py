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


    def add_product(self, value):
        """метод, который будет принимать на вход объект товара и добавлять его в список."""
        self.__product.append(value)


    @property
    def product(self):
        """декоратор для вывода товара в формате"""
        output = " "
        for product in self.__product:
            output += f"{product.name}\n{float(product.price)} шт.\nВ наличии{product.quantity_in_stock} "
        return output


class Product:
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
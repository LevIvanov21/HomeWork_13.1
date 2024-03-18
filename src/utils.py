class Category:
    """Создадим класс "Категории" для вывода товара, его описания"""
    all_quantity_category = 0
    all_quantity_unique_product = 0
    name = str
    description = str
    product = list

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        self.all_quantity_category = 1
        Category.all_quantity_unique_product += 1


class Product:
    """Саздадим класс "Продукт" для развертывания информации о товаре"""
    name = str
    description = str
    price = float
    quantity_in_stock = int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity_in_stock = quantity_in_stock

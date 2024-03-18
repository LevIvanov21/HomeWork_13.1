# Импортируем необходимые пакеты и классы
import pytest
from src.utils import Category
from src.utils import Product

@pytest.fixture
def test_correct_Category():
    return Category("Автомобиль", "Комфортная езда, экономия времени", [1, 2, 3, 4])

# Напишем тест для проверки корректности инициализации объектов класса Category
def test_init_Category(test_correct_Category):
    assert test_correct_Category.name == "Автомобиль"
    assert test_correct_Category.description == "Комфортная езда, экономия времени"
    assert test_correct_Category.product == [1, 2, 3, 4]


@pytest.fixture
def test_correct_init_Product():
    return Product("Subaru Impreza", "Седан, 280 л.с.", 610000.00, 3)

# Напишем тест для проверки корректности инициализации объектов класса Product
def test_Product_method(test_correct_init_Product):
    assert test_correct_init_Product.name == "Subaru Impreza"
    assert test_correct_init_Product.description == "Седан, 280 л.с."
    assert test_correct_init_Product.price == 610000.00
    assert test_correct_init_Product.quantity_in_stock == 3


@pytest.fixture
def test_correct_init_numb():
    return Category("Автомобиль", "Комфортная езда, экономия времени", [1, 2, 3, 4])

# Напишем тест для проверки подсчета продуктов и категории
def test_summ_numb(test_correct_init_numb):
    assert test_correct_init_numb.all_quantity_unique_product == 2
    assert test_correct_init_numb.all_quantity_category == 1

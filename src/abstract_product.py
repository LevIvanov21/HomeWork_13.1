from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    @classmethod
    @abstractmethod
    def build_product(cls, *args, **kwargs):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    def price(self, value):
        pass

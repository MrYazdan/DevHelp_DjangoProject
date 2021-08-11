from unittest import TestCase
from products.models import *


class DiscountTest(TestCase):

    def setUp(self) -> None:
        self.d = Discount


class OffCodeTest(TestCase):

    def setUp(self) -> None:
        self.o = OffCode


class ProductTest(TestCase):

    def setUp(self) -> None:
        self.p = Product

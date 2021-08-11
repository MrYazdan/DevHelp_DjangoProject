from unittest import TestCase
from order.models import *


class StatusTest(TestCase):

    def setUp(self) -> None:
        self.s = Status


class OrderTest(TestCase):

    def setUp(self) -> None:
        self.o = Order


class OrderItemTest(TestCase):

    def setUp(self) -> None:
        self.i = OrderItem

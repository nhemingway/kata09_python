#!/use/bin/env python

import unittest

from checkout import Checkout
from item import Item

items = {
    'A': Item('A', 50, 3, 130),
    'B': Item('B', 30, 2, 45),
    'C': Item('C', 20),
    'D': Item('D', 15),
}

class TestCheckout(unittest.TestCase):
    def price(self, goods):
        co = Checkout(items)
        for item in goods:
            co.scan(item)

        return co.total()

    def test_totals(self):
        self.assertEqual(  0, self.price(""))

        with self.assertRaises( ValueError):
            self.price('foo')

        self.assertEqual( 50, self.price("A"))
        self.assertEqual( 80, self.price("AB"))
        self.assertEqual(115, self.price("CDBA"))
        self.assertEqual(100, self.price("AA"))
        self.assertEqual(130, self.price("AAA"))
        self.assertEqual(180, self.price("AAAA"))
        self.assertEqual(175, self.price("AAABB"))

    def test_incremental(self):
        co = Checkout(items)
        self.assertEqual(  0, co.total())
        co.scan("A");  self.assertEqual( 50, co.total())
        co.scan("B");  self.assertEqual( 80, co.total())
        co.scan("A");  self.assertEqual(130, co.total())
        co.scan("A");  self.assertEqual(160, co.total())
        co.scan("B");  self.assertEqual(175, co.total())

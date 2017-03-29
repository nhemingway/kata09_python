#!/use/bin/env python

import unittest

RULES = """
A     50       3 for 130
B     30       2 for 45
C     20
D     15
"""

import re
from checkout import Checkout

class TestCheckout(unittest.TestCase):
    def price(self, goods):
        co = Checkout(RULES)
        for item in re.split('//', goods):
            co.scan(item)

        return co.total()

    def test_totals(self):
        self.assertEqual(  0, self.price(""))

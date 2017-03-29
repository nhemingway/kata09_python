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

rules_a = [ re.split('\s+', line, 2) for line in re.split("\n", RULES) if line != '']
rules_d = { item[0]: [int(item[1]), item[2:] ] for item in rules_a }

class TestCheckout(unittest.TestCase):
    def price(self, goods):
        co = Checkout(rules_d)
        for item in re.split('//', goods):
            co.scan(item)

        return co.total()

    def test_totals(self):
        self.assertEqual(  0, self.price(""))

        with self.assertRaises( ValueError):
            self.price('foo')

        self.assertEqual( 50, self.price("A"))

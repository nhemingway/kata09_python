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

rules_a = re.split("\n", RULES)
rules_d = dict()
from pprint import pprint
for item in rules_a:
    if item != '':
        m = re.match('(\w+)\s+(\d+)(?:\s+(\d+) for (\d+))?', item)
        if not m:
            raise ValueError('Unparseable price %s' % item)

        key = m.group(1)
        price_1 = int(m.group(2))
        rules_d[key] = { 'price': price_1 }

        if m.group(3) != None:
            offer_count = int(m.group(3))
            offer_price = int(m.group(4))

            rules_d[key]['offer'] = [offer_count, offer_price]

# print 'Rules'
# pprint(rules_d)

class TestCheckout(unittest.TestCase):
    def price(self, goods):
        co = Checkout(rules_d)
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

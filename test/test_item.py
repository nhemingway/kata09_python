#!/usr/bin/env python

import unittest

from item import Item

a = Item('A', 50, 3, 130)

class TestItem(unittest.TestCase):
    def test_a_for_b_offer(self):
        self.assertEqual( (0, 0), a.a_for_b_offer(0))
        self.assertEqual( (0, 1), a.a_for_b_offer(1))
        self.assertEqual( (0, 2), a.a_for_b_offer(2))
        self.assertEqual( (130, 0), a.a_for_b_offer(3))
        self.assertEqual( (130, 1), a.a_for_b_offer(4))
        self.assertEqual( (130, 2), a.a_for_b_offer(5))
        self.assertEqual( (260, 0), a.a_for_b_offer(6))
        self.assertEqual( (260, 1), a.a_for_b_offer(7))

    def test_cost(self):
        self.assertEqual( 0, a.cost(0))
        self.assertEqual( 50, a.cost(1))
        self.assertEqual( 100, a.cost(2))
        self.assertEqual( 130, a.cost(3))
        self.assertEqual( 180, a.cost(4))
        self.assertEqual( 230, a.cost(5))
        self.assertEqual( 260, a.cost(6))
        self.assertEqual( 310, a.cost(7))

import re

class Checkout:
    def __init__(self, rules):
        self._rules = rules
        self._basket = {}

    def scan(self, item):
        if not item:
            return # Might make more sense to raise a ValueError - context!

        if not self._rules.has_key(item):
            raise ValueError('Item %s unknown' % item)

        if not self._basket.has_key(item):
            self._basket[item] = 0

        self._basket[item] += 1

    def total(self):
        # from pprint import pprint
        # pprint(self._basket)

        total = 0
        for item, count in self._basket.items():
            pricing = self._rules[item]

            if 'offer' in pricing:
                offer = pricing['offer']
                [offer_count, offer_price] = offer[:]

                offer_multiple = count / offer_count
                total += offer_multiple * offer_price

                # Adjust count by those items qualifying for the offer
                count -= offer_multiple * offer_count

            total += count * pricing['price']

        return total

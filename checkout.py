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
        import pprint
        pprint.pprint(self._basket)

        total = 0
        for item, count in self._basket.items():
            pricing = self._rules[item]

            total += count * pricing[0]

        return total

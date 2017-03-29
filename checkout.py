class Checkout:
    def __init__(self, rules):
        self._rules = rules
        self._total = 0

    def scan(self, item):
        if not item:
            return 0
        if self._rules.has_key(item):
            pricing = self._rules[item]
        else:
            raise ValueError('Item %s unknown' % item)

        self._total += pricing[0]

    def total(self):
        return self._total

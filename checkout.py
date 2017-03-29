class Checkout:
    def __init__(self, rules):
        self.rules = rules

    def scan(self, item):
        if not item:
            return 0
        if self.rules.has_key(item):
            pricing = self.rules[item]
        else:
            raise ValueError('Item %s unknown' % item)

    def total(self):
        return 0

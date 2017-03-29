class Checkout:
    def __init__(self, catalogue):
        self._catalogue = catalogue
        self._basket = {}

    def scan(self, item):
        if not item:
            return # Might make more sense to raise a ValueError - context!

        if not item in self._catalogue:
            raise ValueError('Item %s unknown' % item)

        if not item in self._basket:
            self._basket[item] = 0

        self._basket[item] += 1

    def total(self):
        total = 0
        for itemname, count in self._basket.items():
            item = self._catalogue[itemname]

            total += item.cost(count)

        return total

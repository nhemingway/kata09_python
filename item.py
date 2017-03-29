class Item:
    def __init__(self, name, price, *offer_args):
        self._name = name
        self._price = price
        if offer_args:
            self._offer = {'count': offer_args[0], 'price': offer_args[1] }
        else:
            self._offer = None

    def cost(self, count):
        (cost, remainder) = self.a_for_b_offer(count)

        cost += remainder * self._price

        return cost

    def a_for_b_offer(self, count):
        remainder = count

        cost = 0

        if self._offer:
            offer_count = self._offer['count']
            offer_price = self._offer['price']

            offer_multiple = count / offer_count
            remainder = count % offer_count

            cost += offer_multiple * offer_price

        return (cost, remainder)



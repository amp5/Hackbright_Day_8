"""This file should have our melon-type classes in it."""

BASE_PRICE = 5

class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    price = BASE_PRICE
    #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price 
        #total = 0   # TODO, calculate the real amount!

        return total


# class Melons(object:)

# watermelons.melons()

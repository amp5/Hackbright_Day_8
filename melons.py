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
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class CanteloupeOrder(object):
    species = "Canteloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    price = BASE_PRICE
    #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total


class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Winter', 'Fall', 'Summer']
    price = BASE_PRICE
    #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price

        price = self.price

        #for order in get_price:
        if self.species == "Casaba" or "Ogen":
            price = price + 1
        elif self.imported == True:
            price = price * 1.5
        elif self.shape == 'square':
            price = price * 2

        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total


class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    price = BASE_PRICE * 1.5
    #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class Santa_ClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    price = BASE_PRICE * 1.5
    #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    price = BASE_PRICE
    #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class Horned_MelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    price = BASE_PRICE * 1.5
    #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']
    price = (BASE_PRICE * 1.5) * 2
    #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    price = BASE_PRICE + 1
    #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

# class Melons(object:)

# watermelons.melons()

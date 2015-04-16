"""This file should have our melon-type classes in it."""

BASE_PRICE = 5

class WatermelonOrder(object):
    """All of the things about this type of order"""

    def __init__(self, species, color, imported, shape, seasons, price):
        self.species = species
        self.color = color
        self.imported = imported
        self.shape = shape
        self.seasons = seasons
        self.price = price


    # species = "Watermelon"
    # color = "green"
    # imported = False
    # shape = 'natural'
    # seasons = ['Fall', 'Summer']
    # price = BASE_PRICE
    # #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class CanteloupeOrder(object):
    def __init__(self, species, color, imported, shape, seasons, price):
        self.species = species
        self.color = color
        self.imported = imported
        self.shape = shape
        self.seasons = seasons
        self.price = price


    # species = "Canteloupe"
    # color = "tan"
    # imported = False
    # shape = 'natural'
    # seasons = ['Spring', 'Summer']
    # price = BASE_PRICE
    # #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total


class CasabaOrder(object):
    
    def __init__(self, species, color, imported, shape, seasons, price):
        self.species = species
        self.color = color
        self.imported = imported
        self.shape = shape
        self.seasons = seasons
        self.price = (price + 1) * 1.5


    # species = "Casaba"
    # color = "green"
    # imported = True
    # shape = 'natural'
    # seasons = ['Spring', 'Winter', 'Fall', 'Summer']
    # price = (BASE_PRICE + 1) * 1.5
    # #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total


class SharlynOrder(object):
    
    def __init__(self, species, color, imported, shape, seasons, price):
        self.species = species
        self.color = color
        self.imported = imported
        self.shape = shape
        self.seasons = seasons
        self.price = price * 1.5



    # species = "Sharlyn"
    # color = "tan"
    # imported = True
    # shape = 'natural'
    # seasons = ['Summer']
    # price = BASE_PRICE * 1.5
    # #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class Santa_ClausOrder(object):
    
    def __init__(self, species, color, imported, shape, seasons, price):
        self.species = species
        self.color = color
        self.imported = imported
        self.shape = shape
        self.seasons = seasons
        self.price = price * 1.5


    # species = "Santa Claus"
    # color = "green"
    # imported = True
    # shape = 'natural'
    # seasons = ['Winter', 'Spring']
    # price = BASE_PRICE * 1.5
    # #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class ChristmasOrder(object):
    def __init__(self, species, color, imported, shape, seasons, price):
        self.species = species
        self.color = color
        self.imported = imported
        self.shape = shape
        self.seasons = seasons
        self.price = price


    # species = "Christmas"
    # color = "green"
    # imported = False
    # shape = 'natural'
    # seasons = ['Winter', 'Spring']
    # price = BASE_PRICE
    # #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class Horned_MelonOrder(object):

    def __init__(self, species, color, imported, shape, seasons, price):
        self.species = species
        self.color = color
        self.imported = imported
        self.shape = shape
        self.seasons = seasons
        self.price = price * 1.5

#     species = "Horned Melon"
#     color = "yellow"
#     imported = True
#     shape = 'natural'
#     seasons = ['Summer']
#     price = BASE_PRICE * 1.5
#     #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class XiguaOrder(object):

    def __init__(self, species, color, imported, shape, seasons, price):
        self.species = species
        self.color = color
        self.imported = imported
        self.shape = shape
        self.seasons = seasons
        self.price = (price * 1.5) * 2

#     species = "Xigua"
#     color = "black"
#     imported = True
#     shape = 'square'
#     seasons = ['Summer']
#     price = (BASE_PRICE * 1.5) * 2
#     #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total

class OgenOrder(object):

    def __init__(self, species, color, imported, shape, seasons, price):
        self.species = species
        self.color = color
        self.imported = imported
        self.shape = shape
        self.seasons = seasons
        self.price = price + 1

#     species = "Ogen"
#     color = "tan"
#     imported = False
#     shape = 'natural'
#     seasons = ['Spring', 'Summer']
#     price = BASE_PRICE + 1
#     #qty = 0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        #qty * price
        total = self.price * qty 
        #total = 0   # TODO, calculate the real amount!

        return total



# Your program should have two separate classes: one to represent a product to be purchased
# and one to represent a shopping cart containing a collection of products.

# Each product has a name, base price, and tax rate.
# There should also be a method to calculate and return the product's total price based
# on the base price and tax rate.
#


class Product:

    def __init__(self, name, base_price, tax_rate, quantity):
        self.name = name
        self.base_price = float(base_price)
        self.tax_rate = tax_rate
        self.quantity = int(quantity)

    def __str__(self):
        return "The {} is ${} plus {} taxes.".format(self.name, '%.2f' % self.base_price, self.tax_rate)

    def total_price(self):
        if self.tax_rate == "standard":
            total = (self.base_price * self.quantity) * 1.13
        elif self.tax_rate == "tax-exempt":
            total = (self.base_price * self.quantity) * 1
        elif self.tax_rate == "imported":
            total = (self.base_price * self.quantity) * 1.25
        return total

# Your program should have two separate classes: one to represent a product to be purchased
# and one to represent a shopping cart containing a collection of products.

# Each product has a name, base price, and tax rate.
# There should also be a method to calculate and return the product's total price based
# on the base price and tax rate.
#


class Product:

    def __init__(self, name, base_price, tax_rate):
        self.name = name
        self.base_price = float(base_price)
        self.tax_rate = float(tax_rate)

    def __str__(self):
        return "The {} is ${} plus {}% in taxes.".format(self.name, '%.2f' % self.base_price, self.tax_rate)

    def total_price(self):
        total = self.base_price + (1 + (self.tax_rate / 100))
        return total

product1 = Product("table", 13.50, 6)
# print(product1)
# print(product1.total_price())
product2 = Product("chair", 5.75, 6)
product3 = Product("whiteboard", 22.25, 6)

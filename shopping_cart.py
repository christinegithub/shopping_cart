# Each shopping cart has a collection of products. It should also have the
# following functionality:
#
# add an product to the cart
# remove an product from the cart
# add up the total cost of all products in the cart before tax
# add up the total cost of all products in the cart after tax
# Think about which class needs to make reference to the other one and remember
# to use a
# import statement accordingly. You don't need it in both files.

from product import Product


class ShoppingCart:

    def __init__(self, products):
        self.products = products

    def __str__(self):
        product_list = ""
        for index, product in enumerate(self.products):
            if index == 0:
                product_list += "Shopping cart: {} x {}".format
                (product.name, product.quantity)
            else:
                product_list += ", {} x {}".format
                (product.name, product.quantity)
        return product_list

    def add_product(self, product):
        return self.products.append(product)

    def remove_product(self, product):
        return self.products.remove(product)

    def total_before_tax(self):
        total_before_tax = 0
        for product in self.products:
            total_before_tax += (product.base_price * product.quantity)
        return '%.2f' % total_before_tax

    def total_after_tax(self):
        total_after_tax = 0
        for product in self.products:
            total_after_tax += product.total_price()
        return '%.2f' % total_after_tax

    def find_expensive(self):
        most_expensive_price = 0
        most_expensive_product = ""

        for product in self.products:
            if product.total_price() > most_expensive_price:
                most_expensive_price = product.total_price()
                most_expensive_product = product.name
        return most_expensive_product


table = Product("table", 13.50, "standard", 1)  # 15.25
chair = Product("chair", 5.75, "tax-exempt", 4)  # 23
whiteboard = Product("whiteboard", 22.25, "tax-exempt", 3)  # 66.75

list_of_products = [table, chair, whiteboard]

shopping_cart = ShoppingCart(list_of_products)

print(shopping_cart)

# Add product
eraser = Product("eraser", 1.05, "imported", 10)  # 13.13
shopping_cart.add_product(eraser)
print(shopping_cart)

# Remove product
shopping_cart.remove_product(chair)
print(shopping_cart)

# Total before taxes (table, whiteboard, eraser)
print(shopping_cart.total_before_tax())

# Total after taxes (table, whiteboard, eraser)
print(shopping_cart.total_after_tax())

# Find most find_expensive
print(shopping_cart.find_expensive())

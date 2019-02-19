# Each shopping cart has a collection of products. It should also have the following functionality:
#
# add an product to the cart
# remove an product from the cart
# add up the total cost of all products in the cart before tax
# add up the total cost of all products in the cart after tax
# Think about which class needs to make reference to the other one and remember to use a
# import statement accordingly. You don't need it in both files.
from product import Product

class ShoppingCart:


    def __init__(self, products):
        self.products = products

    def __str__(self):
        product_list = ""
        for index, product in enumerate(self.products):
            if index == 0:
                product_list += "Shopping cart: {}".format(product.name)
            else:
                product_list += ", {}".format(product.name)
        return product_list

    def add_product(self, product):
        return self.products.append(product)

    def remove_product(self, product):
        return self.products.remove(product)

    def total_before_tax(self):
        total_before_tax = 0
        for product in self.products:
            total_before_tax += product.base_price
        return '%.2f' % total_before_tax

    def total_after_tax(self):
        total_after_tax = 0
        for product in self.products:
            total_after_tax += product.total_price()
        return '%.2f' % total_after_tax

table = Product("table", 13.50, 6)
chair = Product("chair", 5.75, 6)
whiteboard = Product("whiteboard", 22.25, 6)

list_of_products = [table, chair, whiteboard]

shopping_cart = ShoppingCart(list_of_products)

print(shopping_cart)

# Add product
eraser = Product("eraser", 1.05, 6)
shopping_cart.add_product(eraser)
print(shopping_cart)

# Remove product
shopping_cart.remove_product(chair)
print(shopping_cart)

# Total before taxes (table, whiteboard, eraser) 36.80
print(shopping_cart.total_before_tax())

# Total after taxes (table, whiteboard, eraser) 39.00
print(shopping_cart.total_after_tax())
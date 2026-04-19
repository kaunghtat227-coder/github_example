import os
from product import Product

class StoreManager:
    def __init__(self, filename="porducts.txt"):
        self.filename = filename
        self.products = []
        self.load_products()

    def load_products(self):
        self.products = []
        if os.path.isfile(self.filename):
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line !="":
                        parts = line.split(",")
                        name = parts[0]
                        price = int(parts[1])
                        product = Product(name, price)
                        self.products.append(product)

    def save_products(self):
        with open(self.filename, "w") as file:
            for product in self.products:
                file.write(product.to_string() + "\n")

    def create_product(self, product):
        self.products.append(product)
        self.save_products()
        return "Create product successfully."

    def get_products(self):
        return self.products

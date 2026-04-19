class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_string(self):
        return f"{self.name} {self.price}"

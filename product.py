class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self, new_price):
        if new_price < 0:
            return False

        self.price = new_price
        return True

    def update_stock(self, new_stock):
        if new_stock < 0:
            return False

        self.stock = new_stock
        return True

    def __str__(self):
        return f"The product is {self.name}"

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, "
            f"price={self.price}, stock={self.stock})"
        )
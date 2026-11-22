from user import User


class Admin(User):
    def __init__(self, name, email, store):
        super().__init__(name, email)
        self.store = store

    def add_product(self, product):
        self.store.add_product(product)

    def remove_product(self, product):
        return self.store.remove_product(product)

    def update_product_price(self, product, new_price):
        return product.update_price(new_price)

    def update_product_stock(self, product, new_stock):
        return product.update_stock(new_stock)
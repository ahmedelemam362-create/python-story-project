from cart import Cart
from user import User


class Customer(User):
    def __init__(self, name, email, balance, store):
        super().__init__(name, email)

        self.balance = balance
        self.cart = Cart()
        self.store = store

    def add_to_cart(self, product, quantity):
        return self.cart.add_product(product, quantity)

    def remove_from_cart(self, product):
        return self.cart.remove_product(product)

    def buy(self):
        if not self.cart.items:
            print("\nYour cart is empty.")
            return False

        final_total = self.cart.calculate_final_total()

        if final_total > self.balance:
            print("\nInsufficient balance.")
            return False

        for product, quantity in self.cart.items.items():
            if quantity > product.stock:
                print(f"\nNot enough stock for {product.name}.")
                return False

        for product, quantity in self.cart.items.items():
            product.stock -= quantity

        self.balance -= final_total

        print("\n========== PURCHASE ==========")
        print("Purchase successful!")
        print(f"Paid: {final_total}")
        print(f"Remaining balance: {self.balance}")
        print("==============================")

        self.cart.clear_cart()

        return True

    def show_info(self):
        print("\n========== CUSTOMER ==========")
        super().show_info()
        print(f"Balance: {self.balance}")
        print("==============================")
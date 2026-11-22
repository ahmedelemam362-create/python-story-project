class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if quantity <= 0:
            return False

        if quantity > product.stock:
            return False

        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

        return True

    def remove_product(self, product):
        if product not in self.items:
            return False

        del self.items[product]
        return True

    def clear_cart(self):
        self.items.clear()

    def total_quantity(self):
        return sum(self.items.values())

    def calculate_total(self):
        total = 0

        for product, quantity in self.items.items():
            total += product.price * quantity

        return total

    @staticmethod
    def calculate_discount(quantity):
        if quantity >= 5:
            return 0.05
        elif quantity >= 3:
            return 0.03
        return 0

    def calculate_final_total(self):
        total = self.calculate_total()
        quantity = self.total_quantity()

        discount = self.calculate_discount(quantity)

        return total - (total * discount)

    def show_cart(self):
        if not self.items:
            print("\nCart is empty.")
            return

        print("\n========== CART ==========")

        for product, quantity in self.items.items():
            subtotal = product.price * quantity

            print(
                f"{product.name} | "
                f"Quantity: {quantity} | "
                f"Price: {product.price} | "
                f"Subtotal: {subtotal}"
            )

        discount = self.calculate_discount(self.total_quantity())

        print("--------------------------")
        print(f"Total quantity: {self.total_quantity()}")
        print(f"Total: {self.calculate_total()}")
        print(f"Discount: {discount * 100:.0f}%")
        print(f"Final total: {self.calculate_final_total()}")
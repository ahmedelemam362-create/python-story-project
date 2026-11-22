class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            return True

        return False

    def show_products(self):
        if not self.products:
            print("\nNo products available.")
            return

        print("\n========== PRODUCTS ==========")

        for index, product in enumerate(self.products, start=1):
            print(
                f"{index}. {product.name} | "
                f"Price: {product.price} | "
                f"Stock: {product.stock}"
            )

        print("==============================")

    def get_product(self, index):
        if 0 <= index < len(self.products):
            return self.products[index]

        return None
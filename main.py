from product import Product
from story import Store
from customer import Customer
from admin import Admin
from validation import validate_email


ADMIN_EMAIL = "admin@store.com"


def create_products(store):
    laptop = Product("Laptop", 30000, 5)
    mouse = Product("Mouse", 500, 8)
    keyboard = Product("Keyboard", 1500, 6)
    headphones = Product("Headphones", 2000, 10)

    store.add_product(laptop)
    store.add_product(mouse)
    store.add_product(keyboard)
    store.add_product(headphones)


def get_user_info():
    print("\n========== LOGIN ==========")

    name = input("Enter your name: ").strip()

    while True:
        email = input("Enter your email: ").strip()

        if validate_email(email):
            return name, email

        print("Invalid email. Please try again.")


def admin_menu(admin):
    while True:
        print("\n==============================")
        print("          ADMIN MENU")
        print("==============================")
        print("1. Show Products")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Update Product Price")
        print("5. Update Product Stock")
        print("6. My Information")
        print("7. Exit")
        print("==============================")

        choice = input("Choose an option: ")

        if choice == "1":
            admin.store.show_products()

        elif choice == "2":
            name = input("Enter product name: ")

            try:
                price = float(input("Enter product price: "))
                stock = int(input("Enter product stock: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            if price < 0 or stock < 0:
                print("Price and stock cannot be negative.")
                continue

            product = Product(name, price, stock)
            admin.add_product(product)

            print("Product added successfully.")

        elif choice == "3":
            admin.store.show_products()

            try:
                number = int(input("Enter product number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            product = admin.store.get_product(number - 1)

            if product is None:
                print("Invalid product number.")
                continue

            if admin.remove_product(product):
                print("Product removed successfully.")

        elif choice == "4":
            admin.store.show_products()

            try:
                number = int(input("Enter product number: "))
                new_price = float(input("Enter new price: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            product = admin.store.get_product(number - 1)

            if product is None:
                print("Invalid product number.")
                continue

            if admin.update_product_price(product, new_price):
                print("Price updated successfully.")
            else:
                print("Invalid price.")

        elif choice == "5":
            admin.store.show_products()

            try:
                number = int(input("Enter product number: "))
                new_stock = int(input("Enter new stock: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            product = admin.store.get_product(number - 1)

            if product is None:
                print("Invalid product number.")
                continue

            if admin.update_product_stock(product, new_stock):
                print("Stock updated successfully.")
            else:
                print("Invalid stock.")

        elif choice == "6":
            admin.show_info()

        elif choice == "7":
            print("\nGoodbye Admin!")
            break

        else:
            print("Invalid choice.")


def customer_menu(customer):
    while True:
        print("\n==============================")
        print("        CUSTOMER MENU")
        print("==============================")
        print("1. Show Products")
        print("2. Add Product To Cart")
        print("3. Remove Product From Cart")
        print("4. Show Cart")
        print("5. Buy")
        print("6. Customer Information")
        print("7. Exit")
        print("==============================")

        choice = input("Choose an option: ")

        if choice == "1":
            customer.store.show_products()

        elif choice == "2":
            customer.store.show_products()

            try:
                number = int(input("Enter product number: "))
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            product = customer.store.get_product(number - 1)

            if product is None:
                print("Invalid product number.")
                continue

            if customer.add_to_cart(product, quantity):
                print(
                    f"{quantity} x {product.name} "
                    "added to cart."
                )
            else:
                print(
                    "Could not add product. "
                    "Check quantity and stock."
                )

        elif choice == "3":
            customer.cart.show_cart()

            try:
                number = int(
                    input("Enter product number to remove: ")
                )
            except ValueError:
                print("Please enter a valid number.")
                continue

            product = customer.store.get_product(number - 1)

            if product is None:
                print("Invalid product number.")
                continue

            if customer.remove_from_cart(product):
                print("Product removed from cart.")
            else:
                print("Product is not in your cart.")

        elif choice == "4":
            customer.cart.show_cart()

        elif choice == "5":
            customer.buy()

        elif choice == "6":
            customer.show_info()

        elif choice == "7":
            print("\nGoodbye Customer!")
            break

        else:
            print("Invalid choice.")


def main():
    store = Store()

    create_products(store)

    name, email = get_user_info()

    if email.lower() == ADMIN_EMAIL.lower():
        admin = Admin(name, email, store)

        print(f"\nHello Admin, {name}!")
        admin_menu(admin)

    else:
        try:
            balance = float(input("Enter your balance: "))
        except ValueError:
            print("Invalid balance.")
            return

        if balance < 0:
            print("Balance cannot be negative.")
            return

        customer = Customer(
            name,
            email,
            balance,
            store
        )

        print(f"\nHello Customer, {name}!")
        customer_menu(customer)


if __name__ == "__main__":
    main()
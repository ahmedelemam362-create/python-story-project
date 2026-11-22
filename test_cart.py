from product import Product
from cart import Cart


def test_add_product():
    product = Product("Laptop", 30000, 5)
    cart = Cart()

    result = cart.add_product(product, 2)

    assert result is True
    assert cart.items[product] == 2


def test_calculate_total():
    product = Product("Laptop", 30000, 5)
    cart = Cart()

    cart.add_product(product, 2)

    assert cart.calculate_total() == 60000


def test_discount():
    assert Cart.calculate_discount(2) == 0
    assert Cart.calculate_discount(3) == 0.03
    assert Cart.calculate_discount(5) == 0.05
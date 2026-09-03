from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_saucedemo_purchase_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item in items_to_add:
        inventory_page.add_item_to_cart(item)

    assert inventory_page.get_cart_items_count() == 3, (
         "Cart should have 3 items"
    )
    inventory_page.go_to_cart()

    assert cart_page.get_cart_items_count() == 3, (
         "Cart should have 3 items"
    )
    cart_page.proceed_to_checkout()

    checkout_page.fill_checkout_form("Ivan", "Ivanov", "123456")
    checkout_page.continue_checkout()

    total = checkout_page.get_total_amount()

    assert total == "$58.29", f"Expected $58.29, got {total}"

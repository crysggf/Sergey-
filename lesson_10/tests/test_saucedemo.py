"""Тесты для интернет-магазина."""

import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Проверка оформления заказа в интернет-магазине")
@allure.description(
    "Тест проверяет полный сценарий покупки: авторизация, "
    "добавление 3 товаров, оформление заказа и проверка итоговой суммы"
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_purchase_flow(driver):
    """Тест проверки оформления заказа."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открыть страницу авторизации"):
        login_page.open()

    with allure.step("Авторизоваться как standard_user"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить 3 товара в корзину"):
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for item in items_to_add:
            inventory_page.add_item_to_cart(item)

    with allure.step("Проверить, что в корзине 3 товара"):
        assert inventory_page.get_cart_items_count() == 3, (
            "Cart should have 3 items"
        )

    with allure.step("Перейти в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Проверить содержимое корзины"):
        assert cart_page.get_cart_items_count() == 3, (
            "Cart should have 3 items"
        )

    with allure.step("Нажать Checkout"):
        cart_page.proceed_to_checkout()

    with allure.step("Заполнить форму оформления заказа"):
        checkout_page.fill_checkout_form("Ivan", "Ivanov", "123456")
        checkout_page.continue_checkout()

    with allure.step("Получить итоговую сумму"):
        total = checkout_page.get_total_amount()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert total == "$58.29", f"Expected $58.29, got {total}"

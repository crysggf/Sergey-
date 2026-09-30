"""Page Object для главной страницы магазина."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class InventoryPage:
    """Класс для работы с главной страницей магазина."""

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    ITEMS = {
        "Sauce Labs Backpack": {
            "add": (By.ID, "add-to-cart-sauce-labs-backpack")
        },
        "Sauce Labs Bolt T-Shirt": {
            "add": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        },
        "Sauce Labs Onesie": {
            "add": (By.ID, "add-to-cart-sauce-labs-onesie")
        }
    }

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация главной страницы магазина.

        :param driver: экземпляр WebDriver
from        :type driver: WebDriver
        """
        self.driver = driver

    def add_item_to_cart(self, item_name: str) -> "InventoryPage":
        """
        Добавить товар в корзину.

        :param item_name: название товара
        :type item_name: str
        :return: экземпляр текущей страницы
        :rtype: InventoryPage
        """
        if item_name in self.ITEMS:
            add_button: WebElement = self.driver.find_element(
                *self.ITEMS[item_name]["add"]
            )
            add_button.click()
        return self

    def go_to_cart(self) -> "InventoryPage":
        """
        Перейти в корзину.

        :return: экземпляр текущей страницы
        :rtype: InventoryPage
        """
        self.driver.find_element(*self.CART_LINK).click()
        return self

    def get_cart_items_count(self) -> int:
        """
        Получить количество товаров в корзине.

        :return: количество товаров
        :rtype: int
        """
        try:
            badge: WebElement = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0

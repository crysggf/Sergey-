"""Page Object для страницы корзины."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CartPage:
    """Класс для работы со страницей корзины."""

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: экземпляр WebDriver
        :type driver: WebDriver
        """
        self.driver = driver

    def get_cart_items_count(self) -> int:
        """
        Получить количество товаров в корзине.

        :return: количество товаров
        :rtype: int
        """
        items: list[WebElement] = self.driver.find_elements(
            *self.CART_ITEMS
        )
        return len(items)

    def proceed_to_checkout(self) -> "CartPage":
        """
        Нажать кнопку Checkout.

        :return: экземпляр текущей страницы
        :rtype: CartPage
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        return self

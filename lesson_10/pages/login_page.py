"""Page Object для страницы авторизации."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    """Класс для работы со страницей авторизации."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        :param driver: экземпляр WebDriver
        :type driver: WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> "LoginPage":
        """
        Открыть страницу авторизации.

        :return: экземпляр текущей страницы
        :rtype: LoginPage
        """
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        """
        Выполнить авторизацию.

        :param username: имя пользователя
        :type username: str
        :param password: пароль
        :type password: str
        :return: экземпляр текущей страницы
        :rtype: LoginPage
        """
        username_field: WebElement = self.driver.find_element(
            *self.USERNAME_INPUT)
        username_field.clear()
        username_field.send_keys(username)

        password_field: WebElement = self.driver.find_element(
            *self.PASSWORD_INPUT
        )
        password_field.clear()
        password_field.send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

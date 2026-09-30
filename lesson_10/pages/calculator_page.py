"""Page Object для страницы калькулятора."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    DELAY_INPUT = (By.ID, "delay")
    RESULT_SCREEN = (By.CLASS_NAME, "screen")

    BUTTONS = {
        '7': (By.XPATH, "//span[text()='7']"),
        '8': (By.XPATH, "//span[text()='8']"),
        '+': (By.XPATH, "//span[text()='+']"),
        '=': (By.XPATH, "//span[text()='=']"),
    }

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр WebDriver
        :type driver: WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self) -> "CalculatorPage":
        """
        Открыть страницу калькулятора.

        :return: экземпляр текущей страницы
        :rtype: CalculatorPage
        """
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """
        Установить задержку в поле ввода.

        :param seconds: количество секунд задержки
        :type seconds: int
        :return: экземпляр текущей страницы
        :rtype: CalculatorPage
        """
        delay_input: WebElement = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, button_text: str) -> "CalculatorPage":
        """
        Нажать кнопку на калькуляторе.

        :param button_text: текст на кнопке (например '7', '+', '=')
        :type button_text: str
        :return: экземпляр текущей страницы
        :rtype: CalculatorPage
        """
        if button_text in self.BUTTONS:
            button: WebElement = self.driver.find_element(
                *self.BUTTONS[button_text]
            )
            button.click()
        return self

    def get_result(self) -> str:
        """
        Получить результат вычислений с экрана калькулятора.

        :return: текст результата
        :rtype: str
        """
        result_element: WebElement = self.driver.find_element(
            *self.RESULT_SCREEN
        )
        return result_element.text

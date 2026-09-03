from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:

    DELAY_INPUT = (By.ID, "delay")
    RESULT_SCREEN = (By.CLASS_NAME, "screen")

    BUTTONS = {
        '7': (By.XPATH, "//span[text()='7']"),
        '8': (By.XPATH, "//span[text()='8']"),
        '+': (By.XPATH, "//span[text()='+']"),
        '=': (By.XPATH, "//span[text()='=']"),
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get(
         "https://bonigarcia.dev"
         "/""selenium-webdriver-java/slow-calculator.html"
        )
        return self

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, button_text):
        if button_text in self.BUTTONS:
            button = self.driver.find_element(*self.BUTTONS[button_text])
            button.click()
        return self

    def get_result(self):
        # Ждем, пока экран не покажет результат (не "7+8", а число)
        self.wait.until(
            lambda driver: driver.find_element(
                *self.RESULT_SCREEN).text != "7+8"
        )
        result_element = self.driver.find_element(*self.RESULT_SCREEN)
        return result_element.text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        username_field = self.driver.find_element(*self.USERNAME_INPUT)
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

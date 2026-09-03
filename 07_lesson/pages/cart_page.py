from selenium.webdriver.common.by import By


class CartPage:

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def proceed_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        return self

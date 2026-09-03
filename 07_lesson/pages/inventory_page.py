from selenium.webdriver.common.by import By


class InventoryPage:

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

    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        if item_name in self.ITEMS:
            add_button = self.driver.find_element(
                *self.ITEMS[item_name]["add"])
            add_button.click()
        return self

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
        return self

    def get_cart_items_count(self):
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0

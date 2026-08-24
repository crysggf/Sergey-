from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_shop_checkout():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    products = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    for product_id in products:
        product = wait.until(EC.element_to_be_clickable(
            (By.ID, product_id)
        ))
        product.click()

    cart = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "shopping_cart_link")
    ))
    cart.click()

    checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout.click()

    first_name = wait.until(EC.presence_of_element_located(
        (By.ID, "first-name")))
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Петров")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("123456")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    total_element = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "summary_total_label")
    ))
    total = total_element.text

    assert total == "Total: $58.29"

    driver.quit()

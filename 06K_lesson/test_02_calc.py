from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_calculator_delay():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    wait = WebDriverWait(driver, 50)

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    button_7 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='7']")))
    button_7.click()

    button_plus = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='+']")))
    button_plus.click()

    button_8 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='8']")))
    button_8.click()

    button_equal = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='=']")))
    button_equal.click()

    result = wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".screen"), "15"))
    assert result

    driver.quit()

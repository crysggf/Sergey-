from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Сергей")
    Submit_order = driver.find_element(By.CSS_SELECTOR,
                                       "button[type ='Submit']")
    Submit_order.click()
    assert "/post" in driver.current_url

    driver.quit()

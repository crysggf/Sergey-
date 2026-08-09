from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_interaction():
    driver = webdriver.Chrome()
    driver.get(" https://httpbin.qa-territory.online")
    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    assert "/forms/post" in driver.current_url
    driver.back()
    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()

"""Модуль с фикстурами для тестов."""

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture
def driver():
    """
    Фикстура для создания и закрытия драйвера Firefox.

    :yield: экземпляр WebDriver
    :rtype: webdriver.Firefox
    """
    service = FirefoxService(executable_path="geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

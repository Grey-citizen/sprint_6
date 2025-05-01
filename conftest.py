import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@allure.title("Фикстура драйвера")
@pytest.fixture(scope="function")
def webdriver_fixture():
    service = Service(executable_path='/Users/mistg/WebDriver/bin/geckodriver.exe')
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()
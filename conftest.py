import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture(scope="function")
def webdriver_fixture():
    service = Service(executable_path='/Users/mistg/WebDriver/bin/firefox.exe')
    driver = webdriver.firefox(service=service)
    yield driver
    driver.quit()

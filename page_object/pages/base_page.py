from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import webdriver_fixture

class BasePage:
    def __init__(self, webdriver_fixture):
        self.driver = webdriver_fixture
        self.wait = WebDriverWait(webdriver_fixture, 10)

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

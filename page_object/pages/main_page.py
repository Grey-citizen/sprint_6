from page_object.locators.main_page_locators import MainPageLocators
from page_object.data.data import Constants
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from page_object.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver, Constants.MAIN_URL)

    def wait_for_url_to_be(self, url):
        self.wait.until(EC.url_to_be(url),
                                   f"Текущий url не совпадает с ожидаемым:"
                                   f"\n\tТекущий: {self.driver.current_url}"
                                   f"\n\tОжидаемый: {url}")

    def click_on_top_order_button(self):
        self.find_element(MainPageLocators.HEADER_ORDER_BUTTON).click()
        self.wait_for_url_to_be(Constants.ORDER_URL)

    def click_on_order_button(self):
        bottom_order_button_element = self.find_element(MainPageLocators.FOOTER_ORDER_BUTTON)
        self.scroll_to_element(bottom_order_button_element)
        bottom_order_button_element.click()
        self.wait_for_url_to_be(Constants.ORDER_URL)
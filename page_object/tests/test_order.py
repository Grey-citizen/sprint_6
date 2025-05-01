import allure
import pytest
from page_object.pages.order_page import OrderPage
from page_object.locators.order_page_locators import OrderFormLocators
from conftest import webdriver_fixture
from page_object.data.data import Constants, random_name, random_surname, random_address, random_phone
from selenium.webdriver.support import expected_conditions as EC

class TestOrderPage:
    @pytest.mark.repeat(2)
    @allure.title("Позитивное тестирование процесса создания заказа")
    @allure.feature("Страница создания заказа")
    @allure.story("Создание заказа")
    def test_order_page(self, webdriver_fixture):
        name = random_name()
        surname = random_surname()
        address = random_address()
        phone = random_phone()
        page = OrderPage(webdriver_fixture)
        page.set_name(name)
        page.set_surname(surname)
        page.set_address(address)
        page.set_phone(phone)
        page.select_random_metro_station()
        page.click_confirm_button()
        page.set_delivery_date()
        page.set_random_rental_period()
        page.set_random_color_option()

        with allure.step(f"Подтверждаю создание заказа"):
            page.click_confirm_button()
            page.click_confirm_button()
            success_form_element = page.find_element(OrderFormLocators.SUCCESS_MESSAGE)
            assert success_form_element.is_displayed()

    @allure.title("Тест перехода по клику на логотип Яндекс")
    @allure.feature("Логотип Яндекс")
    def test_click_on_yandex_logo(self, webdriver_fixture):
        with allure.step(f"Открываю страницу {Constants.MAIN_URL}"):
            page = OrderPage(webdriver_fixture)

        with allure.step("Проверка перехода на главную страницу dzen"):
            page.click_yandex_logo()
            webdriver_fixture.switch_to.window(window_name=webdriver_fixture.window_handles[1])
            page.wait.until(EC.url_contains('dzen'), "Адрес страницы на новой вкладке не содержит 'dzen'")
            assert "dzen" in webdriver_fixture.current_url, "Адрес страницы на новой вкладке не содержит 'dzen'"
            webdriver_fixture.close()
            webdriver_fixture.switch_to.window(window_name=webdriver_fixture.window_handles[0])

    @allure.title("Тест перехода по клику на логотип Самокат")
    @allure.feature("Логотип Самокат")
    def test_click_on_scooter_logo(self, webdriver_fixture):
        with allure.step(f"Открываю страницу создания заказа"):
            page = OrderPage(webdriver_fixture)

        with allure.step("Проверка перехода на главную страницу Самокат"):
            page.click_samokat_logo()

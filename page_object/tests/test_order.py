import allure
import pytest
from page_object.pages.order_page import OrderPage
from page_object.locators.order_page_locators import OrderFormLocators
from page_object.data import data1, data2


@allure.title('Позитивный сценарий заказа самоката')
class TestOrderFlow:

    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (OrderFormLocators.HEADER_ORDER_BUTTON, data1),
            (OrderFormLocators.FOOTER_ORDER_BUTTON, data2),
        ]
    )
    def test_order_flow(self, driver, locator, order_data):
        main_page = OrderPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_to_element(locator)
        order_page = OrderPage(driver)
        order_page.set_order(order_data)
        assert order_page.check_success_message(), "Всплывающее окно не появилось или сообщение об ошибке."
        order_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Не удалось вернуться на главную страницу 'Самоката'."
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_to_element(locator)
        order_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        assert "zen.yandex.ru" in driver.current_url, "Не удалось открыть главную страницу Дзена."
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
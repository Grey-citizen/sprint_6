import allure
import pytest
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage
from page_object.locators.order_page_locators import OrderFormLocators
from page_object.data import data1, data2

@allure.title('Тесты на проверку вопросов')
class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
            (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
            (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
            (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
            (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
            (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
            (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
        ]
    )
    def test_faq_questions(self, driver, num, result):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_to_question(num)
        assert main_page.get_answer_text(num) == result

    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (OrderFormLocators.HEADER_ORDER_BUTTON, data1),
            (OrderFormLocators.FOOTER_ORDER_BUTTON, data2),
        ]
    )
    def test_create_order(self, driver, locator, order_data):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_to_element(locator)
        order_page = OrderPage(driver)
        order_page.set_order(order_data)
        assert order_page.check_order
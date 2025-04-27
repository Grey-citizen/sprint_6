import allure
from base_page import BasePage
from page_object.locators.order_page_locators import OrderFormLocators


class OrderPage(BasePage):
    @allure.step('Заполнить форму заказа')
    def set_order(self, ame, data):
        self.click_to_element(data['station_locator'])
        self.add_text_to_element(OrderFormLocators.NAME, data['name'])
        self.add_text_to_element(OrderFormLocators.LASTNAME, data['lastname'])
        self.add_text_to_element(OrderFormLocators.ADDRESS, data['address'])
        self.add_text_to_element(OrderFormLocators.PHONE, data['phone'])
        self.click_to_element(OrderFormLocators.NEXT_BUTTON)
        self.click_to_element(OrderFormLocators.WHEN_TO_DELIVER)
        self.add_text_to_element(OrderFormLocators.RENTAL_PERIOD, data['time'])
        for color in data['color']:
            if color in OrderFormLocators.SCOOTER_COLOR_CHECKBOXES:
                self.click_to_element(OrderFormLocators.SCOOTER_COLOR_CHECKBOXES[color])
        self.add_text_to_element(OrderFormLocators.COMMENT, data['comment'])
        self.click_to_element(OrderFormLocators.NEXT_BUTTON)

    def check_order(self, locator):
        return self.get_text_from_element(locator)

    @allure.step('Нажать кнопку Заказать сверху или снизу страницы')
    def click_order_button(self, position):
        if position == 'top':
            self.click_to_element(OrderFormLocators.HEADER_ORDER_BUTTON)
        elif position == 'bottom':
            self.click_to_element(OrderFormLocators.FOOTER_ORDER_BUTTON)

    @allure.step('Проверить сообщение об успешном создании заказа')
    def check_success_message(self):
        return self.is_element_present(OrderFormLocators.SUCCESS_MESSAGE)

    @allure.step('Кликнуть на логотип Самоката')
    def click_scooter_logo(self):
        self.click_to_element(OrderFormLocators.YANDEX_BUTTON)

    @allure.step('Кликнуть на логотип Яндекса и проверить редирект')
    def click_yandex_logo(self):
        yandex_link = self.get_attribute_from_element(OrderFormLocators.YANDEX_BUTTON, 'href')
        self.click_to_element(OrderFormLocators.SCOOTER_BUTTON)
        return yandex_link
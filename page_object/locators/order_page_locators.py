from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

class OrderFormLocators:
    NAME = (By.XPATH, '//input[@placeholder="Введите имя"]')
    LASTNAME = (By.XPATH, '//input[@placeholder="Введите фамилию"]')
    ADDRESS = (By.XPATH, '//input[@placeholder="Введите адрес"]')
    METRO_STATION = (By.XPATH, '//select[@name="station"]')
    PHONE = (By.XPATH, '//input[@placeholder="Введите номер телефона"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    WHEN_TO_DELIVER = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD = (By.XPATH, '//input[@placeholder="Срок аренды"]')
    COMMENT = (By.XPATH, '//input[@placeholder="Комментарий"]')
    SCOOTER_COLOR_CHECKBOXES = {
        'black': (By.XPATH, '//input[@id="color-black"]'),
        'grey': (By.XPATH, '//input[@id="color-grey"]'),
    }
    ORDER_BUTTON = (By.XPATH, '//button[text()="Заказать"]')
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(text(), "Заказ оформлен")]')
    YANDEX_BUTTON = (By.XPATH, '//a[contains(@href, "https://zen.yandex.ru")]')
    SCOOTER_BUTTON = (By.XPATH, '//img[@alt="Scooter logo"]')
    HEADER_ORDER_BUTTON = (By.XPATH, '//button[text()="Заказать"]')
    FOOTER_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM')

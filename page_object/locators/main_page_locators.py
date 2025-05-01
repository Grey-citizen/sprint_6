from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

class MainPageLocators:
    QUESTION_LOCATOR = (By.XPATH, '//div[contains(@class, "accordion__heading")]//button')
    ANSWER_LOCATOR = (By.XPATH, '//div[contains(@class, "accordion__panel")]')
    QUESTION_LOCATOR_TO_SCROLL = (By.XPATH, '//div[contains(@class, "accordion__heading-7")]//button')
    HEADER_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    FOOTER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    class MainPageLocators:
        ACCORDION_SECTION = (By.CLASS_NAME, 'accordion')
        ACCORDION_ITEMS_LOCATOR = (By.CLASS_NAME, "accordion__item")
        ACCORDION_HEADING = (By.CLASS_NAME, 'accordion__heading')
        ACCORDION_PANEL = (By.CLASS_NAME, 'accordion__panel')
        TOP_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
        BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
        SCOOTER_IMG_LOCATOR = (By.XPATH, "//img[@alt='Scooter blueprint']")
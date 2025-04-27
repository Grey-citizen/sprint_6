from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, '//*[@class="accordion__heading-{}"]//button'
    ANSWER_LOCATOR = By.XPATH, '//*[@class="accordion__panel-{}"]'
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, '//div[@class="accordion__heading-7"]//button'
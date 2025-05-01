import pytest
import allure
from selenium.webdriver.common.by import By
import time
from page_object.pages.main_page import MainPage
from page_object.pages.base_page import BasePage
from page_object.data.data import Constants, QA_DATA
from conftest import webdriver_fixture


class TestMainPage:

    @allure.title("Проверка перехода на страницу создания заказа по верхней кнопке")
    @allure.story("Создание заказа")
    @allure.feature("Верхняя кнопка 'Заказать'")
    def test_top_order_button(self, webdriver_fixture):
        with allure.step("Открываем главную"):
            page = MainPage(webdriver_fixture)
        with allure.step("Клик по верхней кнопке 'Заказать'"):
            page.click_on_top_order_button()
        with allure.step("Проверяем, что открылась страница создания заказа"):
            assert webdriver_fixture.current_url == Constants.ORDER_URL

    @allure.title("Проверка перехода на страницу создания заказа по нижней кнопке")
    @allure.story("Создание заказа")
    @allure.feature("Нижняя кнопка 'Заказать'")
    def test_bottom_order_button(self, webdriver_fixture):
        with allure.step("Открываем главную"):
            page = MainPage(webdriver_fixture)
        with allure.step("Клик по нижней кнопке 'Заказать'"):
            page.click_on_order_button()
        with allure.step("Проверяем, что открылась страница создания заказа"):
            assert webdriver_fixture.current_url == Constants.ORDER_URL

    @allure.feature("Вопросы о важном")
    @allure.title("Проверяем секцию «Вопросы о важном»")
    @allure.description(
        "Тест проверяет, что на главной странице присутствуют все вопросы из списка, и что ответы на них отображаются "
        "по клику")
    @pytest.mark.parametrize("qa_data", QA_DATA)
    def test_accordion_item_success(self, webdriver_fixture, qa_data):
        question_text = qa_data["question"]
        answer_text = qa_data["answer"]
        question_xpath = f"//*[contains(text(), '{question_text}')]"
        answer_xpath = f"{question_xpath}/../..//p"

        page = BasePage(webdriver_fixture, Constants.MAIN_URL)
        question_element = page.find_element((By.XPATH, question_xpath))
        answer_element = page.find_element((By.XPATH, answer_xpath))
        page.scroll_to_element(question_element)
        assert answer_element.is_displayed() == False, "Ответ не должен отображаться до клика по вопросу"
        question_element.click()
        time.sleep(0.1)
        assert answer_element.is_displayed() == True, "Ответ должен отображаться после клика по вопросу"
        assert answer_element.text == answer_text, "Текст ответа не совпадает с ожидаемым"
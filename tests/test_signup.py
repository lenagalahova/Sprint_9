import time
import allure
from pages.login_page import LoginPage
from data import name, last_name, email, password
from pages.signup_page import SignupPage


class TestLogin:

    @allure.title("Произошёл ли переход на страницу к формам авторизации")
    def test_going_to_authorization_page(self, driver):
        login_page = LoginPage(driver)
        signup_page = SignupPage(driver)
        user_name = f"user_{int(time.time())}"

        with allure.step("Тап на Создать Аккаунт"):
            login_page.click_to_create_acc()
            signup_page.wait_visible_title()
        with allure.step("Заполнить данные и тап на кнопку Создать"):
            signup_page.fill_all_data(name, last_name, user_name, email, password)
            signup_page.click_to_create_button_down()
            login_page.wait_visible_title()
            url = login_page.get_current_url()
            assert "/signin" in url
            assert login_page.get_login_input_displayed()
            assert login_page.get_password_input_displayed()

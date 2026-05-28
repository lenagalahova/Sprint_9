import time
import allure
from pages.login_page import LoginPage
from data import name, last_name, email, password
from pages.recipes_page import RecipesPage
from pages.signup_page import SignupPage


class TestLogin:
    @allure.title(
        "Произошёл ли переход на главную страницу, отображается ли кнопка «Выход»"
    )
    def test_going_to_main_page(self, driver):
        login_page = LoginPage(driver)
        signup_page = SignupPage(driver)
        recipes_page = RecipesPage(driver)
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

        with allure.step("Заполнить данные формы авторизации"):
            login_page.fill_all_data(user_name, password)
        with allure.step("Нажать Войти"):
            login_page.click_login()
            recipes_page.wait_visible_title()
            current_url = recipes_page.get_current_url()
            assert "/recipes" in current_url
            assert recipes_page.get_logout_button_displayed()

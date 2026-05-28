import allure
from locators.login_page_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators

    @allure.step("Подождать появление страницы")
    def wait_visible_title(self):
        self.wait_visible(self.locators.title_login)

    @allure.step("Кликнуть на Создать аккаунт")
    def click_to_create_acc(self):
        self.click(self.locators.button_create_account)

    @allure.step("Кликнуть на Войти")
    def click_login(self):
        self.click(self.locators.button_login)

    @allure.step("Кликнуть на верхнюю Войти")
    def click_upper_login(self):
        self.click(self.locators.button_upper_login)

    @allure.step("Проверить видимость поля ввода email")
    def get_login_input_displayed(self):
        try:
            return self.find_element(self.locators.input_email).is_displayed()
        except:
            return False

    @allure.step("Проверить видимость поля ввода логина/email")
    def get_password_input_displayed(self):
        try:
            return self.find_element(self.locators.input_password).is_displayed()
        except:
            return False

    @allure.step("Ввести Имя пользователя")
    def set_user_name(self, user_name):
        self.send_keys(self.locators.input_email, user_name)

    @allure.step("Ввести Пароль")
    def set_password(self, password):
        self.send_keys(self.locators.input_password, password)

    @allure.step("Заполнить все поля")
    def fill_all_data(self, user_name, password):
        self.set_user_name(user_name)
        self.set_password(password)

import allure
from locators.signup_page_locators import SignupLocators
from pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SignupLocators

    @allure.step("Подождать появление страницы")
    def wait_visible_title(self):
        self.wait_visible(self.locators.title_signup)

    @allure.step("Ввести Имя")
    def set_name(self, name):
        self.send_keys(self.locators.input_name, name)

    @allure.step("Ввести Фамилию")
    def set_last_name(self, last_name):
        self.send_keys(self.locators.input_last_name, last_name)

    @allure.step("Ввести Имя пользователя")
    def set_user_name(self, user_name):
        self.send_keys(self.locators.input_user_name, user_name)

    @allure.step("Ввести Адрес электронной почты")
    def set_email(self, email):
        self.send_keys(self.locators.input_email, email)

    @allure.step("Ввести Пароль")
    def set_password(self, password):
        self.send_keys(self.locators.input_password, password)

    @allure.step("Тап на Создать аккаунт")
    def click_to_create_button_down(self):
        self.click(self.locators.button_create_down)

    @allure.step("Заполнить все поля")
    def fill_all_data(self, name, last_name, user_name, email, password):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_user_name(user_name)
        self.set_password(password)

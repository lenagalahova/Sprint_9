import os
import allure
from locators.create_recipes_locators import CreateLocators
from pages.base_page import BasePage


class CreatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CreateLocators

    @allure.step("Ввести Название рецепта")
    def set_name_recipe(self, name_recipe):
        self.wait_visible(self.locators.title_create_recipes)
        self.send_keys(self.locators.input_name_recipe, name_recipe)

    @allure.step("Кликнуть на Обед")
    def click_to_lunch(self):
        self.click(self.locators.teg_lunch)

    @allure.step("Кликнуть на Ужин")
    def click_to_dinner(self):
        self.click(self.locators.teg_dinner)

    @allure.step("Ввести Ингредиент")
    def set_ingedient(self, ingedient):
        self.send_keys(self.locators.input_ingidients, ingedient)

    @allure.step("Выбрать первый ингредиент из списка")
    def click_to_ingredient(self):
        self.click(self.locators.input_ingidients_list)

    @allure.step("Ввести количество ингредиента")
    def set_ingedient_count(self, ingedient_count):
        self.send_keys(self.locators.input_ingidients_count, ingedient_count)

    @allure.step("Добавить ингредиент")
    def click_to_add_ingredient(self):
        self.click(self.locators.button_add_ingidients)

    @allure.step("Ввести время")
    def set_time(self, time):
        self.send_keys(self.locators.input_time, time)

    @allure.step("Ввести описание рецепта")
    def set_description(self, description):
        self.send_keys(self.locators.input_description, description)

    @allure.step("Выбрать фото")
    def set_photo(self, image_path):
        file_input = self.find_element(self.locators.input_file)
        file_input.send_keys(image_path)

    @allure.step("Заполнить данные")
    def fill_all_data_recipe(
        self, name_recipe, ingedient, ingedient_count, time, description, image_path
    ):
        self.recipe_title = name_recipe
        self.set_name_recipe(name_recipe)
        self.click_to_dinner()
        self.click_to_lunch()
        self.set_ingedient(ingedient)
        self.click_to_ingredient()
        self.set_ingedient_count(ingedient_count)
        self.click_to_add_ingredient()
        self.set_time(time)
        self.scroll_to_element(self.locators.button_create_recipe_non_active)
        self.set_description(description)
        self.set_photo(image_path)

    @allure.step("Кликнуть на Создать рецепт")
    def click_to_create_recipe(self):
        self.click(self.locators.button_create_recipe)
        self.wait_visible(self.locators.title_recipes_done)

    @allure.step("Проверить видимость карточки рецепта")
    def get_card_recipe_displayed(self):
        try:
            return self.find_element(self.locators.card_of_recipe).is_displayed()
        except:
            return False

    @allure.step("Получить название рецепта со страницы")
    def get_recipe_title(self):
        return self.recipe_title

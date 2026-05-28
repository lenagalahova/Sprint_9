import allure
from locators.recipes_page_locators import RecipesLocators
from pages.base_page import BasePage


class RecipesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RecipesLocators

    @allure.step("Проверить видимость кнопки Выйти")
    def get_logout_button_displayed(self):
        try:
            return self.find_element(self.locators.button_logout).is_displayed()
        except:
            return False

    @allure.step("Кликнуть на Создать рецепт")
    def click_create_recipe(self):
        self.click(self.locators.button_create_recipes)

    @allure.step("Подождать появление страницы")
    def wait_visible_title(self):
        self.wait_visible(self.locators.title_recipes)

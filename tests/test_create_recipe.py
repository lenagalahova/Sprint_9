import allure
import time
from pages.create_recipes_page import CreatePage
from pages.login_page import LoginPage
from data import (
    name,
    last_name,
    email,
    password,
    image_path,
    name_recipe,
    ingedient,
    ingedient_count,
    time_to_create,
    description,
)
from pages.recipes_page import RecipesPage
from pages.signup_page import SignupPage


class TestCreateRecipe:

    @allure.title(
        "Произошёл ли переход на главную страницу, отображается ли кнопка «Выход»"
    )
    def test_going_to_detils_page(self, driver):
        login_page = LoginPage(driver)
        signup_page = SignupPage(driver)
        recipes_page = RecipesPage(driver)
        create_recipe = CreatePage(driver)
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

        with allure.step("Нажать Создать рецепт"):
            recipes_page.click_create_recipe()
        with allure.step("Заполнить данные"):
            create_recipe.fill_all_data_recipe(
                name_recipe, ingedient, ingedient_count, time_to_create, description, image_path
            )
        with allure.step("Нажать Создать рецепт"):
            create_recipe.click_to_create_recipe()
            assert create_recipe.get_card_recipe_displayed()
            actual_title = create_recipe.get_recipe_title()
            assert actual_title == create_recipe.get_recipe_title()

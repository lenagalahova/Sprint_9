from selenium.webdriver.common.by import By

class RecipesLocators:
    title_recipes = (
        By.XPATH,
        './/h1[@class = "styles_title__2fhty" and text()="Рецепты"]',
    )
    button_create_recipes = (
        By.XPATH,
        './/a[@class = "style_link__1kPh8 style_nav__link__2rAY6" and text()="Создать рецепт"]',
    )
    button_logout = (
        By.XPATH,
        './/a[@class = "styles_menuLink__3a59I" and text()="Выход"]',
    )
    title_recipes = (
        By.XPATH,
        './/h1[@class = "styles_title__2fhty" and text()="Рецепты"]',
    )
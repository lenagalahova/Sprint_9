from selenium.webdriver.common.by import By


class CreateLocators:
    title_create_recipes = (
        By.XPATH,
        './/h1[@class = "styles_title__2fhty" and text()="Создание рецепта"]',
    )
    input_name_recipe = (
        By.XPATH,
        './/div[text()="Название рецепта"]/following-sibling::input',
    )
    teg_breakfast = (
        By.XPATH,
        './/button[@class="styles_checkbox__1WBUC styles_checkboxGroupItem__1aTHO styles_checkbox_active__22dG2" and @style="background-color: orange;"]',
    )
    teg_lunch = (
        By.XPATH,
        './/button[@class="styles_checkbox__1WBUC styles_checkboxGroupItem__1aTHO styles_checkbox_active__22dG2" and @style="background-color: green;"]',
    )
    teg_dinner = (
        By.XPATH,
        './/button[@class="styles_checkbox__1WBUC styles_checkboxGroupItem__1aTHO styles_checkbox_active__22dG2" and @style="background-color: purple;"]',
    )
    input_ingidients = (
        By.XPATH,
        './/input[@class = "styles_inputField__3eqTj styles_ingredientsInput__1zzql"]',
    )
    input_ingidients_list = (
        By.XPATH,
        './/div[@class = "styles_container__3ukwm"]/child::div'
    )
    input_ingidients_count = (
        By.XPATH,
        './/input[@class = "styles_inputField__3eqTj styles_ingredientsAmountValue__2matT"]',
    )
    button_add_ingidients = (
        By.XPATH,
        './/div[@class = "styles_ingredientAdd__3fc32"]',
    )
    input_time = (
        By.XPATH,
        './/div[text()="Время приготовления"]/following-sibling::input',
    )
    input_description = (
        By.XPATH,
        './/textarea[@class = "styles_textareaField__1wfhC"]',
    )
    input_photo = (
        By.XPATH,
        './/div[@class = "styles_button__xzu5F"]',
    )
    input_file = (
        By.XPATH,
        './/input[@class = "styles_fileInput__3HjP3"]',
    )
    button_create_recipe_non_active = (
        By.XPATH,
        './/button[@class = "style_button__1FFWl styles_button__f_Q9Z style_button_style_dark-blue__1cpq7 style_button_disabled__3OKp4"]',
    )
    button_create_recipe = (
        By.XPATH,
        './/button[@class = "style_button__1FFWl styles_button__f_Q9Z style_button_style_dark-blue__1cpq7"]',
    )
    title_recipes_done = (
        By.XPATH,
        './/h1[@class = "styles_single-card__title__2QMPq"]',
    )
    card_of_recipe = (
        By.XPATH,
        './/div[@class = "styles_single-card__1yTTj"]',
    )
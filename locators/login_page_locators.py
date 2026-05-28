from selenium.webdriver.common.by import By

class LoginLocators:
    
    title_login = (
        By.XPATH,
        './/h1[@class = "styles_title__2fhty" and text()="Войти на сайт"]',
    )
    button_login = (
        By.XPATH,
        './/a[@class = "style_link__1kPh8 styles_menuLink__3a59I active" and text()="Войти"]',
    )
    button_create_account = (
        By.XPATH,
        './/a[@class="style_link__1kPh8 styles_menuButton__1RUEF" and text()="Создать аккаунт"]',
    )
    input_email = (
        By.XPATH,
        './/input[@type = "text"]',
    )
    input_password = (
        By.XPATH,
        './/input[@type = "password"]',
    )
    button_login = (
        By.XPATH,
        './/button[@class="style_button__1FFWl styles_button__1jD3X style_button_style_dark-blue__1cpq7"]',
    )
    button_upper_login = (
        By.XPATH,
        './/button[class="style_link__1kPh8 styles_menuLink__3a59I active""]',
    )
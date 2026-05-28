from selenium.webdriver.common.by import By


class SignupLocators:
    title_signup = (
        By.XPATH,
        './/h1[@class = "styles_title__2fhty"]',
    )
    input_name = (
        By.XPATH,
        './/div[text()="Имя"]/following-sibling::input',
    )
    input_last_name = (
        By.XPATH,
        './/div[text()="Фамилия"]/following-sibling::input',
    )
    input_user_name = (
        By.XPATH,
        './/div[text()="Имя пользователя"]/following-sibling::input',
    )
    input_email = (
        By.XPATH,
        './/div[text()="Адрес электронной почты"]/following-sibling::input',
    )
    input_password = (
        By.XPATH,
        './/div[text()="Пароль"]/following-sibling::input',
    )
    button_create_upper = (
        By.XPATH,
        './/button[@class = "style_button__1FFWl styles_button__146Sy style_button_style_dark-blue__1cpq7 style_button_disabled__3OKp4"]',
    )
    button_create_down = (
        By.XPATH,
        './/button[@class = "style_button__1FFWl styles_button__146Sy style_button_style_dark-blue__1cpq7"]',
    )

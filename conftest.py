import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from data import URL


@pytest.fixture(scope="function")
def driver():
    options = ChromeOptions()
    options.set_capability('acceptInsecureCerts', True)
    capabilities = {
        "browserName": "chrome",
           "browserVersion": "128.0",
        "selenoid:options": {
            "enableVideo": False
         }
       }
    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        desired_capabilities=capabilities,
        options=options)
    
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()

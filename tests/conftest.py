import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()


@pytest.fixture()
def firefox_headless_mode():
    driver_options = webdriver.FirefoxOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--headless')
    browser.config.driver = webdriver.Firefox(options=driver_options)

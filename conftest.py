from selenium import webdriver
from selenium.webdriver.firefox import options
import pytest
from base_page.main_page import MainPage
from base_page.order_page import OrderPage
import data


@pytest.fixture(autouse=True)
def driver(request):
    firefox_options = options.Options()
    firefox_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=firefox_options)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(data.url)
    return page

@pytest.fixture(autouse=True)
def order_page(driver):
    page = OrderPage(driver)
    page.go_to_url(data.url)
    return page
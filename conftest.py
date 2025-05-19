from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from config.data import GenerateData


@pytest.fixture(autouse=True)
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()



@pytest.fixture(autouse=True)
def setup(request):
    generate_data = GenerateData()
    request.instance.email = generate_data.generate_email()
    request.instance.password = generate_data.generate_password()
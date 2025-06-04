from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8, poll_frequency=1)
        self.fake = Faker("ru_RU")

    def go_to_url(self, url):
        self.driver.get(url)

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        self.wait.until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click_to_element(self, some):
        self.wait.until(EC.element_to_be_clickable(some))
        self.driver.find_element(*some).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def my_drag_and_drop(self, locator_from, locator_to):
        element_from = self.find_element_with_wait(locator_from)
        element_to = self.find_element_with_wait(locator_to)
        self.driver.drag_and_drop(element_from, element_to).perform()


    def back_to_previous_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])


    def go_to_last_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
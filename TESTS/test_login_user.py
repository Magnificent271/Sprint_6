from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators


class TestLoginUser():
    def test_login_user(self, driver):
        wait = WebDriverWait(driver, 8, poll_frequency=1)
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys("vadim@gmail.com")
        wait.until(EC.element_to_be_clickable(Locators.PASSWORD_INPUT)).send_keys(123)
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_all_elements_located(Locators.CARDS_IN_MAIN_PAGE))
        assert wait.until(EC.presence_of_element_located(Locators.NAME_REGISTRED_USER)).text == "User."
        assert wait.until(EC.visibility_of_element_located(Locators.ICON_USER_PROFILE)).is_displayed()
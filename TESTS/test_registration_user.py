import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators



# Тест регистрации пользователя
class TestUserRegistration(Locators):
    def test_user_registration(self, driver):
        email = self.email
        password = self.password
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_AND_REGISTRATION_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.NOT_ACCOUNT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON)).click()
        self.wait.until(EC.visibility_of_all_elements_located(self.CARDS_IN_MAIN_PAGE))
        assert self.wait.until(EC.presence_of_element_located(self.NAME_REGISTRED_USER)).text == "User."
        assert self.wait.until(EC.visibility_of_element_located(self.ICON_USER_PROFILE)). is_displayed()



class TestNotRegistration(Locators):

    @pytest.mark.parametrize("email, password", [
        ("test@test@test.comm", "123123"),   # email не по маске
        ("vadim@gmail.com", "123"),          # зарегистрированный пользователь
    ])



    def test_not_registration(self, driver, email, password):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8, poll_frequency=1)
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_AND_REGISTRATION_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.NOT_ACCOUNT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON)).click()
        assert self.wait.until(EC.visibility_of_all_elements_located(self.REGISTRATION_INPUT_ERROR))
        assert self.wait.until(EC.visibility_of_element_located(self.REGISTRATION_ERROR_MESSAGE)). is_displayed()



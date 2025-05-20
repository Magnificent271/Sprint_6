import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators



# Тест регистрации пользователя
class TestUserRegistration():
    def test_user_registration(self, driver):
        email = self.email
        password = self.password
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NOT_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys(email)
        wait.until(EC.element_to_be_clickable(Locators.PASSWORD_INPUT)).send_keys(password)
        wait.until(EC.element_to_be_clickable(Locators.CONFIRM_PASSWORD_INPUT)).send_keys(password)
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_all_elements_located(Locators.CARDS_IN_MAIN_PAGE))
        assert wait.until(EC.presence_of_element_located(Locators.NAME_REGISTRED_USER)).text == "User."
        assert wait.until(EC.visibility_of_element_located(Locators.ICON_USER_PROFILE)). is_displayed()



class TestNotRegistration():

    @pytest.mark.parametrize("email, password", [
        ("test@test@test.comm", "123123"),   # email не по маске
        ("vadim@gmail.com", "123"),          # зарегистрированный пользователь
    ])



    def test_not_registration(self, driver, email, password):
        wait = WebDriverWait(driver, 8, poll_frequency=1)
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NOT_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys(email)
        wait.until(EC.element_to_be_clickable(Locators.PASSWORD_INPUT)).send_keys(password)
        wait.until(EC.element_to_be_clickable(Locators.CONFIRM_PASSWORD_INPUT)).send_keys(password)
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
        assert wait.until(EC.visibility_of_all_elements_located(Locators.REGISTRATION_INPUT_ERROR))
        assert wait.until(EC.visibility_of_element_located(Locators.REGISTRATION_ERROR_MESSAGE)). is_displayed()



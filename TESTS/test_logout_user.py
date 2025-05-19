from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators



class Test_Logout_User(Locators):
    def test_logout_user(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8, poll_frequency=1)
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_AND_REGISTRATION_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT)).send_keys("vadim@gmail.com")
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys(123)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        assert self.wait.until(EC.visibility_of_element_located(self.LOGIN_AND_REGISTRATION_BUTTON)).is_displayed()
        assert self.wait.until(EC.invisibility_of_element_located(self.NAME_REGISTRED_USER))
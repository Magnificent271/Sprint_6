from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators
from config.data import PRODUCT_NAME



class TestCreateAdNotLoginUser(Locators):
    def test_create_ad_not_login_user(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8, poll_frequency=1)
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        self.wait.until(EC.element_to_be_clickable(self.CREATE_AD_BUTTON)).click()
        message = self.wait.until(EC.visibility_of_element_located(self.CREATE_AD_MASSAGE))
        assert message.text == "Чтобы разместить объявление, авторизуйтесь", \
            f"Ожидаемое сообщение не совпадает. Получено: {message.text}"



class TestCreateAdLoginUser(Locators):
    def test_create_ad_login_user(self, driver):
        email = self.email
        password = self.password
        product_name = PRODUCT_NAME
        self.driver = driver
        self.wait = WebDriverWait(driver, 8, poll_frequency=1)
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_AND_REGISTRATION_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.NOT_ACCOUNT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD_INPUT)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(self.NAME_REGISTRED_USER))
        self.wait.until(EC.element_to_be_clickable(self.CREATE_AD_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.CREATE_AD_NAME_INPUT)).send_keys(product_name)
        self.wait.until(EC.element_to_be_clickable(self.CREATE_AD_PRICE_INPUT)).send_keys(1000)
        self.wait.until(EC.element_to_be_clickable(self.CREATE_AD_DESCRIPTION_TEXT_AREA)).send_keys('Машинка в хорошем состоянии')
        self.wait.until(EC.element_to_be_clickable(self.CREATE_AD_DROPDOWN_CATEGORY)).click()
        self.wait.until(EC.element_to_be_clickable(self.CREATE_AD_DROPDOWN_CATEGORY_OPTION)).click()
        self.wait.until(EC.element_to_be_clickable(self.CREATE_AD_RADIO_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.CREATE_AD_BUTTON_CREATE)).click()
        self.wait.until(EC.presence_of_element_located(self.NAME_REGISTRED_USER))
        self.wait.until(EC.visibility_of_all_elements_located(self.CARDS_IN_MAIN_PAGE))
        self.wait.until(EC.visibility_of_element_located(self.ICON_USER_PROFILE)).click()
        element = self.wait.until(EC.presence_of_element_located(self.CARDS_USER_AD)).text
        assert element == product_name
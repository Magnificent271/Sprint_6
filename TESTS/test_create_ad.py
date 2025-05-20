from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators
from config.data import PRODUCT_NAME



class TestCreateAdNotLoginUser():
    def test_create_ad_not_login_user(self, driver):
        wait = WebDriverWait(driver, 8, poll_frequency=1)
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_BUTTON)).click()
        message = wait.until(EC.visibility_of_element_located(Locators.CREATE_AD_MASSAGE))
        assert message.text == "Чтобы разместить объявление, авторизуйтесь", \
            f"Ожидаемое сообщение не совпадает. Получено: {message.text}"



class TestCreateAdLoginUser():
    def test_create_ad_login_user(self, driver):
        email = self.email
        password = self.password
        product_name = PRODUCT_NAME
        wait = WebDriverWait(driver, 8, poll_frequency=1)
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.NOT_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.EMAIL_INPUT)).send_keys(email)
        wait.until(EC.element_to_be_clickable(Locators.PASSWORD_INPUT)).send_keys(password)
        wait.until(EC.element_to_be_clickable(Locators.CONFIRM_PASSWORD_INPUT)).send_keys(password)
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
        wait.until(EC.presence_of_element_located(Locators.NAME_REGISTRED_USER))
        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_NAME_INPUT)).send_keys(product_name)
        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_PRICE_INPUT)).send_keys(1000)
        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_DESCRIPTION_TEXT_AREA)).send_keys('Машинка в хорошем состоянии')
        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_DROPDOWN_CATEGORY)).click()
        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_DROPDOWN_CATEGORY_OPTION)).click()
        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_RADIO_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_BUTTON_CREATE)).click()
        wait.until(EC.presence_of_element_located(Locators.NAME_REGISTRED_USER))
        wait.until(EC.visibility_of_all_elements_located(Locators.CARDS_IN_MAIN_PAGE))
        wait.until(EC.visibility_of_element_located(Locators.ICON_USER_PROFILE)).click()
        element = wait.until(EC.presence_of_element_located(Locators.CARDS_USER_AD)).text
        assert element == product_name
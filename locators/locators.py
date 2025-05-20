from selenium.webdriver.common.by import By


class Locators:

    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    NOT_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Введите Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Повторите пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    NAME_REGISTRED_USER = (By.XPATH, "//h3[@class='profileText name']")
    ICON_USER_PROFILE = (By.XPATH, "//button[@class='circleSmall']")
    REGISTRATION_INPUT_ERROR = (By.XPATH, "//div[@class='input_inputError__fLUP9']")
    REGISTRATION_ERROR_MESSAGE = (By.XPATH, "//span[text()='Ошибка']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    CREATE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    CREATE_AD_MASSAGE = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    CREATE_AD_NAME_INPUT = (By.XPATH, "//input[@placeholder='Название']")
    CREATE_AD_PRICE_INPUT = (By.XPATH, "//input[@placeholder='Стоимость']")
    CREATE_AD_DESCRIPTION_TEXT_AREA = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    CREATE_AD_DROPDOWN_CATEGORY = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CREATE_AD_DROPDOWN_CATEGORY_OPTION = (By.XPATH, "//div[2]/div/button[@class='dropDownMenu_btn__o8ARs dropDownMenu_noDefault__wSKsP'][2]")
    CREATE_AD_DROPDOWN_LOCATION = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CREATE_AD_DROPDOWN_LOCATION_OPTION = (By.XPATH, "//div[3]/div/button[@class='dropDownMenu_btn__o8ARs dropDownMenu_noDefault__wSKsP'][4]")
    CREATE_AD_RADIO_BUTTON = (By.XPATH, "//div[@class='radioUnput_inputRegular__FbVbr']")
    CREATE_AD_BUTTON_CREATE = (By.XPATH, "//button[text()='Опубликовать']")
    CARDS_USER_AD = (By.XPATH, "//div[@class='card'][last()]/div/div[@class='about']/h2")
    CARDS_IN_MAIN_PAGE = (By.XPATH, "//div[@class='card']")





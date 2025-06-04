from selenium.webdriver.common.by import By



class MainPageLocators:

    QUESTION_LOCATOR = (By.XPATH, "//div[@id='accordion__heading-{}']")
    QUESTION_LOCATOR_TO_SCROLL = (By.XPATH, "//div[@id='accordion__heading-7']")
    ANSWER_LOCATOR = (By.XPATH, "//div[@id='accordion__panel-{}']/p")
    ORDER_BUTTON_1 = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")
    ORDER_BUTTON_2 = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    LOGO_SCOOTER_LOCATOR = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    LOGO_YANDEX_LOCATOR = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    LOGO_DZEN_LOCATOR = (By.XPATH, "//a[@aria-label='Логотип Бренда']")
    MAIN_PAGE_TITLE = (By.XPATH, "//div[@class='Home_Header__iJKdX']")
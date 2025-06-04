from selenium.webdriver.common.by import By



class OrderScooterLocators:
    FIRST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_STATION_VALUE = (By.XPATH, "//button[.//div[text()='Сокольники']]")
    METRO_STATION_VARIABLE_VALUE = (By.CLASS_NAME, "Order_Text__2broi")
    PHONE_NUMBER_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, "//div[@class='Order_NextButton__1_rCA']/button[text()='Далее']")
    DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    PERIOD_DROPDOWN_VALUE = (By.CLASS_NAME, 'Dropdown-option')
    SCOOTER_COLOR_BLACK = (By.XPATH, "//label[@for='black']")
    SCOOTER_COLOR_GREY = (By.XPATH, "//label[@for='grey']")
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    MODAL_CONFIRM_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Да']")
    MODAL_ORDER_CONFIRMED_MESSAGE = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    VIEW_ORDER_BUTTON = (By.XPATH, "//div[@class='Order_NextButton__1_rCA']/button[text()='Посмотреть статус']")
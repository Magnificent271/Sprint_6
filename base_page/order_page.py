from base_page.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderScooterLocators
from selenium.webdriver.common.keys import Keys
from helper import HelpFunctions
import allure
import random
import data



class OrderPage(BasePage):


    @allure.step("Клик на кнопку Заказать")
    def click_to_order_button(self, num):
        locator_name = f"ORDER_BUTTON_{num}"
        locator = getattr(MainPageLocators, locator_name)
        self.scroll_to_element(locator)
        self.click_to_element(locator)

    @allure.step("Ввод персональных данных")
    def entering_personal_data(self):
        fake_name = self.fake.first_name()
        fake_last_name = self.fake.last_name()
        self.add_text_to_element(OrderScooterLocators.FIRST_NAME_INPUT, fake_name)
        self.add_text_to_element(OrderScooterLocators.LAST_NAME_INPUT, fake_last_name)

    @allure.step("Ввод адреса")
    def entering_address_data(self):
        self.add_text_to_element(OrderScooterLocators.ADDRESS_INPUT, data.city)
        self.click_to_element(OrderScooterLocators.METRO_STATION_INPUT)
        index = random.randint(1, 50)
        metro_station = self.find_elements_with_wait(OrderScooterLocators.METRO_STATION_VARIABLE_VALUE)
        metro_station[index].click()

    @allure.step("Ввод номера телефона")
    def entering_phone_number(self):
        phone = HelpFunctions.phone_number()
        self.add_text_to_element(OrderScooterLocators.PHONE_NUMBER_INPUT, phone)


    @allure.step("Ввод даты заказа")
    def entering_order_date(self):
        date = HelpFunctions.date()
        self.add_text_to_element(OrderScooterLocators.DATE_INPUT, date)
        self.find_element_with_wait(OrderScooterLocators.DATE_INPUT).send_keys(Keys.ENTER)


    @allure.step("Выбор срока аренды")
    def entering_rental_period(self):
        self.click_to_element(OrderScooterLocators.RENTAL_PERIOD_DROPDOWN)
        self.find_elements_with_wait(OrderScooterLocators.PERIOD_DROPDOWN_VALUE)[0].click()

    @allure.step("Выбор цвета самоката")
    def entering_scooter_color(self):
        self.click_to_element(OrderScooterLocators.SCOOTER_COLOR_BLACK)

    @allure.step("Ввод комментария")
    def entering_comment(self):
        self.add_text_to_element(OrderScooterLocators.COMMENT_INPUT, "Комментарий к тестовому заказу")

    @allure.step("Ввод данных для заказа")
    def entering_order_data(self):
        self.entering_personal_data()
        self.entering_address_data()
        self.entering_phone_number()
        self.click_to_element(OrderScooterLocators.NEXT_BUTTON)
        self.entering_order_date()
        self.entering_rental_period()
        self.entering_scooter_color()
        self.entering_comment()
        self.click_to_element(OrderScooterLocators.CONFIRM_ORDER_BUTTON)
        self.click_to_element(OrderScooterLocators.MODAL_CONFIRM_BUTTON)

    @allure.step("Проверка сообщения об успешном заказе")
    def check_message_order_success(self):
        confirm_message = self.find_element_with_wait(OrderScooterLocators.MODAL_ORDER_CONFIRMED_MESSAGE)
        return confirm_message.is_displayed()

    @allure.step("Клик на кнопку Просмотреть заказ")
    def click_to_view_order_button(self):
        self.click_to_element(OrderScooterLocators.VIEW_ORDER_BUTTON)

    @allure.step("Клик на логотип Яндекса")
    def click_to_yandex_logo(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX_LOCATOR)

    @allure.step("Клик на логотип Самоката")
    def click_to_scooter_logo(self):
        self.click_to_element(MainPageLocators.LOGO_SCOOTER_LOCATOR)

    @allure.step("Проверка отображения логотипа Дзен")
    def check_dzen_logo_is_displayed(self):
        return self.find_element_with_wait(MainPageLocators.LOGO_DZEN_LOCATOR).is_displayed()

    @allure.step("Проверка отображения логотипа Самоката")
    def check_scooter_logo_is_displayed(self):
        return self.find_element_with_wait(MainPageLocators.MAIN_PAGE_TITLE).is_displayed()

    @allure.step("Переход на страницу Дзен")
    def check_go_to_page_dzen(self):
        self.click_to_view_order_button()
        self.click_to_yandex_logo()
        self.go_to_last_tab()


    @allure.step("Переход на страницу Самоката")
    def check_go_to_page_scooter(self):
        self.back_to_previous_tab()
        self.click_to_scooter_logo()

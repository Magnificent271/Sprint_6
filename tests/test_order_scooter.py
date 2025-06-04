import pytest
import allure


@allure.title("Тесты проверки заказа самоката")
@allure.title("Проверка переходов на страницу Дзен и Самоката")
@allure.description("")
@allure.severity(allure.severity_level.CRITICAL)
class TestOrderPage:

    @pytest.mark.parametrize('num', [1, 2])


    def test_order_scooter(self, order_page, num):
        order_page.click_to_order_button(num)
        order_page.entering_order_data()
        assert order_page.check_message_order_success
        order_page.check_go_to_page_dzen()
        assert order_page.check_dzen_logo_is_displayed
        order_page.check_go_to_page_scooter()
        assert order_page.check_scooter_logo_is_displayed

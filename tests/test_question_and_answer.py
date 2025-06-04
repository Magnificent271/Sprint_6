import pytest
import allure
import data


@allure.title("Тесты проверки вопросов и ответов")
@allure.description("")
class TestMainPage:

    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])


    def test_question_and_answer(self, main_page, num):
        assert main_page.check_question_and_answer(num) == data.question_and_answer[num]
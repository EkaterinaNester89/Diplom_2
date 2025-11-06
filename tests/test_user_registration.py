import allure
import pytest

from data.user import UserData
from helpers.user import UserAPIHelper


class TestUserCreate:
    @allure.title("Проверка успешное создание пользователя")
    def test_user_create_account_shows_ok_true_200(self):
        user_api = UserAPIHelper()
        data = user_api.generate_user_create_data(keys=["name", "email", "password"])
        response = user_api.send_request_create(data)
        assert response.status_code == 200
        assert response.json().get("success")

    @allure.title("Проверка нельзя создать двух одинаковых пользователей ")
    def test_user_create_account_shows_ok_false_403(self):
        user_api = UserAPIHelper()
        data = user_api.generate_user_create_data(keys=["name", "email", "password"])
        user_api.send_request_create(data)
        with allure.step("Используем такие же данные для регистрации кроме пароля"):
            data.update(
                {
                    "password": "password" + user_api.generate_random_string(23),
                }
            )
            response = user_api.send_request_create(data)

            assert response.status_code == 403
            assert response.json() == UserData.USER_CREATE_ALREADY_EXISTS_ERROR_403

    @pytest.mark.parametrize(
        "test_case, keys",
        [
            pytest.param(
                "Проверка если email нет - запрос возвращает ошибку",
                ["name", "password"],
                id="without_email",
            ),
            pytest.param(
                "Проверка если пароля нет - запрос возвращает ошибку",
                ["email", "name"],
                id="without_password",
            ),
        ],
    )
    @allure.title("{test_case}")
    def test_user_create_account_missing_fields_shows_error_403(self, test_case, keys):
        user_api = UserAPIHelper()

        data = user_api.generate_user_create_data(keys=keys)
        response = user_api.send_request_create(data)

        assert response.status_code == 403
        assert response.json() == UserData.USER_CREATE_MISSING_FIELD_ERROR_403

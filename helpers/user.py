import allure
import requests

from data.user import UserUrls
from helpers.common import CommonApiHelper


class UserAPIHelper(CommonApiHelper):
    @allure.step("Отправка запроса для регистрирования пользователя в системе")
    def send_request_create(self, data):
        return requests.request(url=UserUrls.USER_CREATE_URL[0],
                                method=UserUrls.USER_CREATE_URL[1],
                                json=data)

    @allure.step("Отправка запроса для входа пользователя в систему")
    def send_request_login(self, data):
        return requests.request(url=UserUrls.USER_LOGIN_URL[0],
                                method=UserUrls.USER_LOGIN_URL[1],
                                json=data)
    @allure.step("Получение данных нового тестового пользователя")
    def data_random_new_user_account(self, keys=None):
        data = self.generate_user_create_data(keys=keys)
        response = self.send_request_create(data)
        if response.status_code == 201:
            return data

    @allure.step("Создание тестовых данных пользователя")
    def generate_user_create_data(self, keys=None):
        name = self.generate_random_string(23)
        password = self.generate_random_string(23)
        email = f"{self.generate_random_string(15)}@{self.generate_random_string(15)}notexists.com"

        full_data = {"name": name, "password": password, "email": email}

        if keys is None:
            return full_data

        return {k: full_data[k] for k in keys if k in full_data}

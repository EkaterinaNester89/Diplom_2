import random

import allure
import requests

from data.ingredients import IngredientData
from data.order import OrderData
from .common import CommonApiHelper


class OrderAPIHelper(CommonApiHelper):
    @allure.step("Отправка запроса для создания заказа в системе")
    def send_request_create(self, data, headers=None):
        return requests.request(
            url=OrderData.ORDER_CREATE_URL[0],
            method=OrderData.ORDER_CREATE_URL[1],
            json=data,
            headers=headers,
        )

    @allure.step("Отправка запроса для получения списка ингредиентов из системы")
    def send_request_get_ingredients(self):
        response = requests.request(
            url=IngredientData.INGREDIENT_GET_LIST_URL[0],
            method=IngredientData.INGREDIENT_GET_LIST_URL[1],
        )
        if response.status_code == 200:
            response_json = response.json()
            data = response_json["data"]
            output = []
            for ingredient in data:
                output.append(ingredient["_id"])
            return output

    @allure.step("Создание тестовых данных заказа")
    def generate_order_create_data(self):
        ingredients = self.send_request_get_ingredients()
        return {"ingredients": random.sample(ingredients, 2)}

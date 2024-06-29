import pytest
import allure
import requests
import datas

class TestCreateOrder:

    @allure.title('Успешное создание заказа с авторизацией пользователя')
    def test_order_successful_creating(self, user, get_ingredients):
        payload = {'ingredients': [get_ingredients[0], get_ingredients[1], get_ingredients[2]]}
        headers = {'Authorization': user['access_token']}
        response = requests.post(datas.BASE_URL + datas.Endpoints['USER_ORDER'], data=payload, headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert 'number' in response.json()['order'] and isinstance(response.json()['order']['number'], int)

    @allure.title('Успешное создание заказа без авторизации пользователя')
    def test_orders_unauthorized_user_successful_creating(self, get_ingredients):
        payload = {'ingredients': [get_ingredients[0], get_ingredients[1], get_ingredients[2]]}
        response = requests.post(datas.BASE_URL + datas.Endpoints['USER_ORDER'], data=payload)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert 'number' in response.json()['order'] and isinstance(response.json()['order']['number'], int)


    @allure.title('Проверка создания заказа без ингредиентов')
    def test_orders_without_ingredients_failed(self, user):
        payload = {'ingredients': []}
        headers = {'Authorization': user['access_token']}
        response = requests.post(datas.BASE_URL + datas.Endpoints['USER_ORDER'], data=payload, headers=headers)
        assert response.status_code == 400
        assert response.json().get("success") is False
        assert response.json()['message'] == datas.Messages['INGREDIENTS_NOT_PROVIDED']


    @allure.title('Проверка создания заказа с некорректно заданным ингредиентом')
    def test_orders_wrong_ingredient_failed(self, user):
        payload = {'ingredients': ["wrong"]}
        headers = {'Authorization': user['access_token']}
        response = requests.post(datas.BASE_URL + datas.Endpoints['USER_ORDER'], data=payload, headers=headers)
        assert response.status_code == 500
        assert datas.Messages['INTERNAL_SERVER_ERROR'] in response.text

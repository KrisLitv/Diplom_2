import pytest
import allure
import requests
import datas
import helpers

class TestUpdateUser:

    @allure.title('Успешная проверка изменения почты существующего пользователя')
    @allure.step('Изменение почты пользователя')
    def test_user_changed_email_successful_result(self, user):
        new_email = helpers.generate_random_login()
        payload = {'email': new_email}
        headers = {'Authorization': user['access_token']}
        response = requests.patch(datas.BASE_URL + datas.Endpoints['USER_INFO'], data=payload, headers=headers)

        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"
        response_data = response.json()

        assert 'user' in response_data, "В теле ответа отсутствует ключ 'user'"
        assert 'email' in response_data['user'], "В теле ответа отсутствует ключ 'email' внутри 'user'"
        assert response_data['user']['email'] == new_email, f"Ожидался email {new_email}, но получен {response_data['user']['email']}"


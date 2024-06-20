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


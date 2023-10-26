from http import HTTPStatus

import allure
import pytest

from user_api import UsersClient
from users import (DefaultUser, UserDict)
from schema import validate_schema



@allure.feature('Users')
@allure.story('Users API')
class TestUsers:
    @allure.title('Create user and get user by user name')
    def test_create_get_user(self, client: UsersClient):
        payload = DefaultUser()
        response = client.create_user_api(payload)
        json_response: UserDict = response.json()
        assert response.status_code == HTTPStatus.CREATED

        response_get = client.get_user_api(payload['username'])
        assert response.status_code == HTTPStatus.OK

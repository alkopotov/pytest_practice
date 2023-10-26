from base_request import BaseRequest
import pprint
import json
import requests
import pytest
import allure
from pydantic import BaseModel, Field
from fakers import random_number, user_name, first_name, last_name, email, password, phone



class DefaultUser(BaseModel):
    id: int = Field(default_factory=random_number)
    username: str = Field(
        default_factory=user_name
    )
    first_name: str = Field(
        alias='firstName',
        default_factory=first_name
    )
    last_name: str = Field(
        alias='lastName',
        default_factory=last_name
    )
    email: str = Field(
        default_factory=email
    )
    password: str = Field(
        default_factory=password
    )
    phone: str = Field(
        default_factory=phone
    )
    user_status: int = Field(
        alias='userStatus',
        default_factory=random_number
    )


# print(DefaultUser().model_dump(by_alias=True))

user_data = [DefaultUser().model_dump(by_alias=True) for _ in range(10)]

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL_PETSTORE)


@pytest.mark.parametrize('item', user_data)
@allure.story('Test User')
def test_api(item):
    data = json.dumps(item)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE_URL_PETSTORE + '/user/', data=data, headers=headers)
    pprint.pprint(response.text)
    get_user = base_request.get('user', item['username'])
    assert item['id'] == get_user['id']
    assert item['username'] == get_user['username']
    assert item['firstName'] == get_user['firstName']
    assert item['lastName'] == get_user['lastName']
    assert item['email'] == get_user['email']
    assert item['password'] == get_user['password']
    assert item['phone'] == get_user['phone']
    assert item['userStatus'] == get_user['userStatus']

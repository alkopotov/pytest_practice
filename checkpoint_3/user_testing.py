from base_request import BaseRequest
import pprint
import json
import requests
import pytest

user_data = [
    {
        "id": 1,
        "username": "piter",
        "firstName": "Piter",
        "lastName": "Gregory",
        "email": "piter@me.com",
        "password": "piter$123",
        "phone": "+900 928 00 12",
        "userStatus": 1
    },
    {
        "id": 2,
        "username": "gavin",
        "firstName": "Gavin",
        "lastName": "Belson",
        "email": "belson@me.com",
        "password": "gavin$123",
        "phone": "+400 123 25 67",
        "userStatus": 2
    },
    {
        "id": 3,
        "username": "russ",
        "firstName": "Russ",
        "lastName": "Hannemann",
        "email": "thebest@russ.com",
        "password": "$ghk$123",
        "phone": "+100 678 12 90",
        "userStatus": 2
    },
    {
        "id": 4,
        "username": "richard",
        "firstName": "Richard",
        "lastName": "Hendrics",
        "email": "richard@piedpiper.com",
        "password": "$hjkh-12Aesdf-o&%3hjO0",
        "phone": "+213 124 00 91",
        "userStatus": 1
    }
]


BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL_PETSTORE)


@pytest.mark.parametrize('item', user_data)
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



from base_request import BaseRequest
import pprint
import json
import requests
import pytest
import allure
from pydantic import BaseModel, Field
from fakers import random_number, status, timestamp, heads_or_tail



class DefaultOrder(BaseModel):
    id: int = Field(default_factory=random_number)
    pet_id: int = Field(alias='petId', default_factory=random_number)
    quantity: int = Field(default_factory=random_number)
    ship_date: str = Field(alias='shipDate', default_factory=timestamp)
    status: str = Field(default_factory=status)
    complete: bool = Field(default_factory=heads_or_tail)


order_data = [DefaultOrder().model_dump(by_alias=True) for _ in range(10)]


BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL_PETSTORE)


@pytest.mark.parametrize('item', order_data)
@allure.story('Test Store')
def test_api(item):
    data = json.dumps(item)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE_URL_PETSTORE + '/store/order', data=data, headers=headers)
    pprint.pprint(response.text)
    get_order = base_request.get('store/order', str(item['id']))
    assert item['id'] == get_order['id']
    assert item['petId'] == get_order['petId']
    assert item['quantity'] == get_order['quantity']
    assert item['shipDate'] == get_order['shipDate']
    assert item['status'] == get_order['status']
    assert item['complete'] == get_order['complete']

import requests
import pprint
import json

data = {
    "id": 25,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "Charlie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

response = requests.get(f'https://petstore.swagger.io/v2/pet/25')
pprint.pprint('Запрашиваем объект')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.json())

data_json = json.dumps(data)
headers = {"Content-Type": "application/json"}
response_put = requests.post(f'https://petstore.swagger.io/v2/pet/', data=data_json, headers=headers)
pprint.pprint('Обновляем объект')
pprint.pprint(response_put.reason)
pprint.pprint(response_put.status_code)
pprint.pprint(response_put.text)

response = requests.get(f'https://petstore.swagger.io/v2/pet/25')
pprint.pprint('Проверяем объект')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.json())

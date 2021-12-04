"""
3. добавить файл test_find_pets.py
в файле вспомогательная функция get_pets_by_status
и параметризованная тестовая функция
test_positive со значением status ["available", "pending", "sold"]
Выполнить проверки на response через assert:
a. статус код
b. проверить все ли элементы из response имеют status соответствующий из запроса
"""

import requests
import json
import pytest


def get_pets_by_status(status):
    api_method = f'v2/pet/findByStatus?status={status}'
    url = f'https://petstore.swagger.io/{api_method}'
    headers = {'accept': 'application/json'}

    response = requests.request("GET", url, headers=headers)
    return response


@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_positive(status):
    resp = get_pets_by_status(status)
    resp_dict = resp.json()

    # print(type(resp_dict))
    # print(resp_dict)
    # print(*resp_dict[0]['status'])

    assert resp.status_code == 200, 'Код ответа не соответствует ожидаемому'
    assert resp_dict[0]['status'] == status, f'Поле status не соответствует ожидаемому {status}, ожидаемое - {resp_dict[0]["status"]}'




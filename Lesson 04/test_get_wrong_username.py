"""
4. добавить файл test_get_wrong_username,
выполнить негативный сценарии в параметризованной тестовой функции test_negative,
параметризовать по значению username со значениями 'wrong', 'error'
метод get_user должен вернуть нам 404 ошибку
с сообщением User not found
выполнить assertы на статус код, значение полей из response: type, message
"""
import requests
import json
import pytest


def get_user(username):
    api_method = f'v2/user/{username}'
    url = f'https://petstore.swagger.io/{api_method}'
    headers = {'accept': 'application/json'}

    response = requests.request("GET", url, headers=headers)
    return response


@pytest.mark.parametrize("username", ['wrong', 'error'])
def test_negative(username):
    res = get_user(username)
    print(res)
    resp_dict = res.json()

    assert res.status_code == 404, 'Код ответа не соответствует ожидаемому'
    assert resp_dict['type'] == "error", f'Поле status не соответствует ожидаемому {"error"}, ожидаемое - {resp_dict["type"]}'
    assert resp_dict['message'] == "User not found", f'Поле status не соответствует ожидаемому {"User not found"}, ожидаемое - {resp_dict["message"]}'
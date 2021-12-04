"""2. добавить файл test_add_pet,
 в котором добавляем 2 вспомогательные функции: post_pet и delete_pet
 далее создаем тестовую функцию test_positive,
 внутри тестовой функции выполняем следующие шаги:
 a. Предусловие. сгенерировать данные для запроса POST/v2/pet,
 а именно: id, category, name, photoUrls, tags, status
 b. Выполнение запроса. вызвать нашу вспомогательную функцию post_pet
 которую создали ранее в параметрах передать значении id, category, name, photoUrls, tags, status
 с. Постусловие. удалить ранее созданный объект Pet,
 для этого вызываем вспомогательную функцию delete_pet
 в параметрах функции передаем pet_id
 d. выполнить проверки через assert для response ручки POST/v2/pet:
 статус код == 200
 значение status в запросе и в ответе должны совпадать
 значение name в запросе и в ответе должны совпадать"""

import requests
import json


def post_pet(id, name, photoUrls, status):
    api_method = "v2/pet"
    url = "https://petstore.swagger.io/" + api_method

    # header for POST
    header = {'accept': 'application/json'}
    header["content-type"] = "application/json"

    # формируем тело запроса
    req_dict = {
        "id": id,
        "category": {
            "id": id,
            "name": name
        },
        "name": name,
        "photoUrls": [
            photoUrls
        ],
        "tags": [
            {
                "id": id,
                "name": name
            }
        ],
        "status": status
    }

    response = requests.request("POST", url, headers=header, json=req_dict)
    resp_dict = response.json()
    # делаем проверки
    assert response.status_code == 200, 'Код ответа не соответствует ожидаемому'
    assert resp_dict['name'] == name, f'Поле name не соответствует ожидаемому {name}, ожидаемое - {resp_dict["Smart"]}'

    return response


def delete_pet(id):
    api_method = f"/v2/pet/{id}"
    url = f'https://petstore.swagger.io/{id}'
    header = {'accept': 'application/json'}
    response = requests.request("DELETE", url, headers=header)


def test_positive():
    id = 2
    name = 'Smart'
    photoUrls = 'https://petstore/1'
    status = 'available'
    post_pet(id, name, photoUrls, status)
    delete_pet(id)

test_positive()

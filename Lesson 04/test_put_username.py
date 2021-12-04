"""
5. автоматизировать ручку PUT/v2/user/{username},
для этого мы должны выполнить следующие шаги
a. создать пользователя,
данные для тело запроса генерируем рандомно:
user_id, username, firstName, lastName, email, password, phone
b. выполнить get запрос чтоб получить данные пользователя
которого создалии ранее
c. из response изменить значение в поле phone,
выполнить put запрос
d. еще раз выполнить get запрос чтоб получить новые значение ранее созданного пользователя
e. выполнить проверку изменилось ли значение в поле phone
"""

import random
import requests
import json
import pytest


def post_user(id, username, firstname, lastname, email, password, phone, userStatus=0):
    api_method = "v2/user"
    url = "https://petstore.swagger.io/" + api_method

    header = {"Accept": "application/json"}
    header["content-type"] = "application/json"

    req_dict = {
        "id": id,
        "username": username,
        "firstName": firstname,
        "lastName": lastname,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": userStatus
    }

    response = requests.request("POST", url, headers=header, json=req_dict)

    return response


def get_user(username):
    api_method = f'v2/user/{username}'
    url = f'https://petstore.swagger.io/{api_method}'
    headers = {'accept': 'application/json'}

    response = requests.request("GET", url, headers=headers)
    resp_dict = response.json()
    return resp_dict


def put_user(username):
    api_method = f'v2/user/{username}'
    url = f'https://petstore.swagger.io/{api_method}'
    headers = {'accept': 'application/json'}
    headers["content-type"] = "application/json"

    resp = post_user(id, username, firstname, lastName, email, password, phone, userStatus=0)
    resp_dict = resp.json()
    resp_dict['phone'] = phone_1

    response = requests.request("PUT", url, headers=headers, json=resp_dict)
    return response


username_list = ['Bob', 'Matt', 'Sam', 'Cruel', 'Smart']
firstname_list = ['Kate', 'Ivan', 'Mikhael', 'Max', 'Varya', 'Ann']
lastName_list = ['Johns', 'Klark', 'Smith', 'Raider']
email_list = ['bob@mail.ru', '123456@mail.ru', '8546@mail.ru', 'bob879@mail.ru', 'bo58464@mail.ru']

id = random.randint(1, 300)
username = random.choice(username_list)
firstname = random.choice(firstname_list)
lastName = random.choice(lastName_list)
email = random.choice(email_list)
password = random.randint(0, 600)
phone = random.randint(658798, 6547875555)
phone_1 = random.randint(785214, 6547875555)

print(post_user(id, username, firstname, lastName, email, password, phone, userStatus=0))
r = get_user(username)
print(r)
p = put_user(username)
print(p)
g = get_user(username)
print(g)


"""1 task
установить библиотеку requests,
выполнить get запрос,
напечатать статус код и json структуру из response в swagger petstore, ручки:
a. GET/pet/findByStatus, значение для параметра status='available'
b. GET/user/username, значение для параметра username='string'
"""
import requests
import json

url_aval = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available'
response = requests.get(url_aval)
print(response.status_code)
print(response.json())

url_user = 'https://petstore.swagger.io/v2/user/string'
resp = requests.get(url_user)
print(resp.status_code)
print(resp.json())

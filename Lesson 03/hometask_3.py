"""1. создать функции area, circumference, volume
каждая из них принимает аргумент радиус
создать эти функции через четвертую функцию wrapper
которая возвращает lambda функцию
посмотрите на формулы каждой функции,
найдите общее чтоб могли определять все 3 функции в одном wrapper
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
volume = 4/3 * math.pi * radius ** 3
"""
import math


def wrapper(n):
    return lambda x, y, z: print(x + ' ' + y + ' ' + z), area(n), circumference(n), volume(n)


def area(radius):
    a = math.pi * radius ** 2
    return a


def circumference(radius):
    c = 2 * math.pi * radius
    return c


def volume(radius):
    v = 4 / 3 * math.pi * radius ** 3
    return v


print(wrapper(20))

"""2. создать список из 100 элементов, 
случайные числа от -50 до 50, 
записать в файл "numbers.txt" положительные элементы 
считать числа из файла 
посчитать среднее арифметическое
"""

import random as rn
import numpy

a = [rn.randint(-50, 50) for i in range(100)]

with open(r'numbers.txt', 'w') as file:
    b = [x for x in a if x > 0]
    for i in b:
        file.write(str(i))

with open(r'numbers.txt', 'r') as f:
    data = f.read()
    list_data = list(map(int, data))
    print("Среднее арифметичское: " + str(numpy.mean(list_data)))

"""3. создать список слов из 1000 элементов, 
получить слова из списка words 
рассчитать вероятность для каждого слова
words =['hello', 'python', 'good', 'car', 'bye', 'sleep', 'python', 'car', 'python']
"""
from collections import Counter

words = ['hello', 'python', 'good', 'car', 'bye', 'sleep', 'python', 'car', 'python']
words_1000 = words * 112  # 1000/len(words) получили число, на которое нужно умножить список words
del words_1000[0:8]  # удаляем лишние элементы, чтобы получилось ровно 1000
print(len(words_1000))

print(*words, sep='\n')
cnt = Counter(words)
print(cnt)
print('\n Word\t Probability')
for k, v in cnt.items():
    print('{0}\t{1} %'.format(k, v * 100 / len(words)))

"""
4. читать файл words.txt добавить в словарь, где ключи - английские слова, 
значения - русские слова 
написать программу которая состоит из 2 режимов (train/test) 
- в train пользователь вводит с консоли слова на английском и на русском, 
добавляете в файл новые слова 
- в test пользователь вводит с консоли слово на английском языке программа печатает перевод слова на русском языке.
создать файл words.txt в папке проекта, сохранить следующий текст.
hello - привет
apple - яблоко
big - большой
list - список
orange - апельсин
table - стол
cup - крушка
mouse - мышь
phone - телефон
pen - ручка
brain - мозг
paper - бумага

"""
words_dict = {
    'hello': 'привет',
    'apple': 'яблоко',
    'big': 'большой',
    'list': 'список',
    'orange': 'апельсин',
    'table': 'стол',
    'cup': 'кружка',
    'mouse': 'мышь',
    'phone': 'телефон',
    'pen': 'ручка',
    'brain': 'мозг',
    'paper': 'бумага'
}

f = open(r'words.txt', 'w', encoding='utf-8')  # создали файл words.txt
for key, value in words_dict.items():
    f.write(f'\n{key}: {value}')
f.close()
with open(r'words.txt', 'r', encoding='utf-8') as f:  # считали файл
    data = f.read()
    print(data)

add_words = dict() # создаем пустой словарь, из текстового сюда добавлять слова и перевод


def train(english_word, translate_russian):
    """

    :param english_word: вводим английское слово
    :param translate_russian: вводим русское слово
    :return:
    Добавляем слова в текстовый файл
    """
    file = open(r'words.txt', 'a', encoding='utf-8')
    file.write(f'\n{english_word}: {translate_russian}')
    file.close()



def add_words_in_dict():
    """

    :return:
    Считываем из текстового файла значения и добавляем в словарь.
    """
    with open(r'words.txt', 'r', encoding='utf-8') as rf:
        lines = rf.readlines()
        for i in lines:
            k = i.strip().split(':')[0]
            v = i.strip().split(':')[1:]
            add_words.update({k: v})


def test(en_word):
    """

    :param en_word: вводим английское слово
    :return:
    Поиск слова по ключу в словаре
    """
    if en_word in add_words.keys():
        print('Перевод английского слова ', en_word, '-', add_words[en_word][0])
    else:
        print('Такого слова нет в словаре')

while True:
    print('Добро пожаловать в программу "Словарь"\n Нажмите 1 - для добавления слов\n Нажмите 2 - для перевода слов\n Нажмите 3 - для выхода')
    push = int(input())
    if push == 1:
        en_word = input("Введите слово на английском: \n ")
        tr_russian = input("Введите перевод слова: \n ")
        train(en_word, tr_russian)
        add_words_in_dict()
        with open(r'words.txt', 'r', encoding='utf-8') as f:  # считали файл
            data = f.read()
            print("\nСловарь:\n", data)
        continue
    if push == 2:
        word = input('Введите слово для перевода: \n')
        add_words_in_dict()
        test(word)
        continue
    else:
        print('Выход из программы')
        break
"""
6. создать класс Wolf с атрибутами: скорость, вес, цвет 
- добавить к классу Wolf метод get_power, возвращающий мощность power = speed**2 / weight 
- создать 100 объектов класса Wolf исходные значение взять рандомно из диапазона значений 
- найти самого сильного волка из списка

speed in range(20, 200)
weight in range(30, 70)
color = ['white', 'black', 'gray', 'ginger', 'brown']
"""
import random


class Wolf:
    def __init__(self, speed, weight, color):
        self.speed = speed
        self.weight = weight
        self.color = color

    def get_power(self):
        power = self.speed ** 2 / self.weight
        return power


color = ['white', 'black', 'gray', 'ginger', 'brown']
max_strong_wolf = []
list_strong_wolves = [Wolf(random.randint(20, 200), random.randint(30, 70), random.choice(color)) for i in range(100)]
b = [i.get_power() for i in list_strong_wolves]
c = dict(zip(list_strong_wolves, b))
max_strong = max(b)
strong_wolf = [k for k, v in c.items() if v == max_strong]

print('Самый сильный волк: ', strong_wolf , 'c мощностью: ', max_strong)

"""
 7.
 создать классы Nokia, Iphone, Samsung, 
 унаследованные от класса Phone 
 аргументы в конструтурах классов: 
 Phone - color, price, name 
 Nokia - color, price, count_buttons 
 Samsung - color, price, waterproofness 
 Iphone - color, price, speed_internet 
 в нижеприведенном блоке создается 120 объектов класса Iphone, 
 105 объектов класса Samsung, 
 75 объектов класса Nokia, 
 запустить этот код и убедиться что все классы правильно определны

from random import *
colors = ["red", "black", "white", "golden", "silver"]
speed_internet = ["2G", "3G", "4G", "5G"]
waterproofness = [True, False]
list_Iphone = [Iphone(choice(colors), randint(15000, 110000), choice(speed_internet)) for i in range(120)]
list_Sam = [Samsung(choice(colors), randint(8000, 90000), choice(waterproofness)) for i in range(105)]
list_Nokia = [Nokia(choice(colors), randint(3000, 25000), randint(24, 56)) for i in range(75)]
"""

from random import *


class Phone:
    def __init__(self, color, price, name):
        self.color = color
        self.price = price
        self.name = name


class Nokia(Phone):
    def __init__(self, color, price, count_buttons):
        self.color = color
        self.price = price
        self.count_buttons = count_buttons


class Iphone(Phone):
    def __init__(self, color, price, speed_internet):
        self.color = color
        self.price = price
        self.speed_internet = speed_internet


class Samsung(Phone):
    def __init__(self, color, price, waterproofness):
        self.color = color
        self.price = price
        self.waterproofness = waterproofness


colors = ["red", "black", "white", "golden", "silver"]
speed_internet = ["2G", "3G", "4G", "5G"]
waterproofness = [True, False]
list_Iphone = [Iphone(choice(colors), randint(15000, 110000), choice(speed_internet)) for i in range(120)]
list_Sam = [Samsung(choice(colors), randint(8000, 90000), choice(waterproofness)) for i in range(105)]
list_Nokia = [Nokia(choice(colors), randint(3000, 25000), randint(24, 56)) for i in range(75)]

# проверка отработки методов класса
Iph = [i.speed_internet for i in list_Iphone]
Sam = [i.waterproofness for i in list_Sam]
Nok = [i.count_buttons for i in list_Nokia]
print(*Iph)
print(*Sam)
print(*Nok)

"""8. 
создайте функцию print_triangle, 
которая принимает число и выводит следующий шаблон
n = 5
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1, 
например для n=5"""
n=5

def print_triangle(num):
    b = [i for i in range(1, n+1)]
    x = 0
    for i in b:
        x -= 1
        print(*b[x::-1])

print_triangle(n)
"""
9. создать функцию my_sqrt, 
которая вычисляет квадратный корень из числа, 
если число меньше нуля, 
поднимает исключение ValueError 
с сообщением "impossible to got negative number"
"""
import math

class ValueError(Exception):
    pass

def my_sqrt(a):
    if a < 0:
        raise ValueError("impossible to got negative number")
    res = math.sqrt(a)
    return res

print(my_sqrt(25))
print(my_sqrt(-11))

"""
10. создать функцию circumference, 
которая вычисляет длину окружности 
если радиус меньше нуля поднимает собственное исключение DistanceError 
с сообщением 'radius can`t less than 0
"""
import math

class DistanceError(Exception):
    pass

def circumference(radius):
    if radius < 0:
        raise DistanceError('radius can`t less than 0')
    return 2 * math.pi * radius

print(circumference(20))
print(circumference(-1))






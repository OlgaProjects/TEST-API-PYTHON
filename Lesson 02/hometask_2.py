"""
    task 1
    даны 3 числа, напечатайте четные числа
"""

a, b, c = 5, 10, 64
even_list = []
even_list.append(a)
even_list.append(b)
even_list.append(c)
even = [i for i in even_list if i % 2 == 0]
print(even)

"""
    task 2
    введите из консоли слово, если длина больше 5 символов, выведите три буквы посередине
"""

word = input("Введите слово: \n")

if len(word) > 5:
    a = len(word) // 2
    b = a - 1
    c = a + 2
    print(word[b:c])

"""
    task 3
    дано число, если больше 100 выведите «more», если в диапазоне 10-100 выведите «mid», иначе выведите «low»
"""
a = 76

if a > 100:
    print('More')
elif 100 > a > 10:
    print('Mid')
else:
    print('low')
"""
    или с тернарным оператором
"""
a = 'more' if a > 100 else 'Mid' if 100 > a > 10 else 'low'
print(a)

"""
    task 4
    введите из консоли длину и ширину дома, 
    рассчитайте площадь, если площадь больше 100, 
    напечатайте «большой дом», 
    иначе выведите «маленький дом»
"""

length = int(input("Введите длину дома: \n"))
width = int(input("Введите ширину дома: \n"))

square = length * width
result = 'Большой дом' if square > 100 else 'маленький дом'
print(result)

"""
    task 5
    создайте функцию для определение гипотенузы если заданы катеты в аргументах
"""
import math

def hypotenuse(kat1, kat2):
    res = math.sqrt(kat1**2 + kat2**2)
    return res

print(hypotenuse(4,3))

"""
    task 6
    создайте функцию для нахождение корней квадратного уравнения
"""
import math

def equation_square_root(a, b, c):
    """
    :param a: коэффициент a
    :param b: коэффициент b
    :param c: коэффициент c
    :return: корни квадратного уравнения ax2 + bx + c = 0
    вычисляем дискриминант discriminant
    вычисляем корень дискриминанта root
    Если discriminant > 0, то квадратное уравнение имеет два корня; если discriminant = 0, то 1 корень.
    Если discriminant < 0, то корней нет.

    """
    discriminant = b ** 2 - 4 * a * c
    root = math.sqrt(discriminant)
    if discriminant > 0:
        x1 = (-b + root) / (2 * a)
        x2 = (-b - root) / (2 * a)
        print(f"Результаты: x1 = {x1}, x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"Резльтат: x = {x}" )
    else:
        print("Корней нет")

print("Вычисляем корни квадратного уравнения для: ax2 + bx + c = 0 \n")
while True:
    a = float(input("Введите коэффициент a, где а не равно 0: \n"))
    if a != 0:
        b = float(input("Введите коэффициент b: \n"))
        c = float(input("Введите коэффициент c: \n"))
        res = equation_square_root(a, b, c)
        break
    else:
        print("Число а не должно равняться 0")
    continue

"""
    task 7
    создайте функцию для вычисления евклидово расстояние

"""

from scipy.spatial import distance

def euclid_distance(a, b):
    """
    :param a: кортеж 1 представляемых точек
    :param b: кортеж 2 представляемых точек
    :return: результат вычисления евклидового расстояния

    """
    dst = distance.euclidean(a, b)
    return dst

a = (1, 2, 3)
b = (4, 5, 6)

print(euclid_distance(a, b))

"""or 
    print(math.dist(a, b))
    or 
    print(math.sqrt(sum((a - b)**2 for a, b in zip(a, b))))
"""

"""
    task 9
    создать список из 50 случайных чисел от 10 до 40. 
    найти все числа, которые делятся на 2 и 5 без остатка

"""

import random as rn

a = [rn.randint(10, 50) for i in range(50)]
print(a)

b = [i for i in a if i % 2 == 0 and i % 5 == 0]
print(b)

"""
    task 10
    создать словарь из 5 элементов, 
    значения - случайный список из 10 чисел, найти суммы всех списков

"""
import random as rn

random_values = {}

x = [rn.randint(1, 1000) for i in range(10)]
y = [rn.randint(1, 1000) for i in range(10)]
z = [rn.randint(1, 1000) for i in range(10)]
r = [rn.randint(1, 1000) for i in range(10)]
v = [rn.randint(1, 1000) for i in range(10)]

random_values['a'] = x
random_values['b'] = y
random_values['c'] = z
random_values['d'] = r
random_values['e'] = v

t = []

for key, val in random_values.items():
    for i in random_values[key]:
        t.append(i)

print(sum(t))

"""
    task 11
    Русское лото 
    у вас есть список из 4 чисел (например 4, 78, 99, 872). 
    Cоздаете бесконечный цикл в котором генерируется случайное число в диапазоне от 0 до 1000 
    остановить цикл тогда, когда выпадут все числа из нашего билета, посчитать количество попыток

"""
import random as rn

tiсket = [4, 78, 99, 872]
t = 0
end_list = set()

while len(tiсket) != len(end_list):
    b = rn.randint(0, 1000)
    t += 1
    for i in tiсket:
        if b == i:
            end_list.add(b)

print('Число попыток: ', t)
print(list(end_list))


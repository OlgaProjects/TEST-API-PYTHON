import numpy

'''First task'''
word_1 = 'Face'
word_2 = 'Elipse'

a = word_1.find('F')
b = word_2.find('E')

if a != -1 and b != -1:
    print('True')

'''2 task'''
import numpy

age_alex = 15
age_semen = 30
age_milana = 45
age_list = []
age_list.append(age_alex)
age_list.append(age_semen)
age_list.append(age_milana)
a = numpy.mean(age_list)
print('Средний возраст: ' + str(a))

'''3 task'''
word_1 = 'Faceapp'
word_2 = 'Elipse'
a = word_1.find('a')
if len(word_1) > len(word_2) and a != -1:
    print('True')

'''4 task'''
word_1 = 'Faceapp'
word_2 = 'Elipse'
a = len(word_1) + len(word_2)
print('+' * a)

'''5 task'''
nums = [1, 3, 2, 5, 4, 12, 4, 34, 5]

print(max(nums))
print(min(nums))
print(len(nums))
print(sum(nums))

'''6 task'''

city = ["Moscow", "Nalchik", "Kazan", "Ufa", "Samara"]

print(city.index("Nalchik"))

city = [x for x in city if not 'a' in x]
print(city)

'''7 task'''
phones = ["88123045131", "88123045193", "88123045313", "88123045692", "88123045697",
          "88123046019", "88123046103", "88123046105", "88123046909", "88123046926",
          "88123047036", "88123047634", "88123047714", "88123047810", "88123047911",
          "88123047986", "88123048023", "88123048249", "88123048255", "88123048343", "88123048467",
          "88123048565", "88123048594", "88123048255", "88123048343", "88123048467",
          "88123049405", "88123049421", "88123049429", "88123049432", "88123049433",
          "88123049491", "88123049500", "88123049517", "88123049522"]

phones_done = ["88123045193", "88123045313", "88123045692", "88123046019", "88123046103",
               "88123046105", "88123046909", "88123046926", "88123047036", "88123047714",
               "88123047810", "88123047911", "88123048023", "88123048249", "88123048343",
               "88123048467", "88123048565", "88123048594", "88123048255", "88123048343",
               "88123049405", "88123049421", "88123049429", "88123049432", "88123049433",
               "88123049491", "88123049517", "88123049522"]
a = set(phones)
b = set(phones_done)

a = a.difference(b)
print(a)

'''8 task'''

phones1 = ["88123045131", "88123045193", "88123045313", "88123045692", "88123045697",
           "88123046019", "88123046103", "88123046105", "88123046909", "88123046926",
           "88123047036", "88123047634", "88123047714", "88123047810", "88123047911",
           "88123047986", "88123048023", "88123048249", "88123048255", "88123048343", "88123048467",
           "88123048565", "88123048594", "88123048255", "88123048343", "88123048467",
           "88123049405", "88123049421", "88123049429", "88123049432", "88123049433",
           "88123049491", "88123049500", "88123049517", "88123049522"]

phones2 = ["88123045131", "88123049652", "88123045313", "88123045692", "88123049748",
           "88123046019", "88123049870", "88123046105", "88123046909", "88123049902",
           "88123047036", "88123047634", "88123050020", "88123047810", "88123047911",
           "88123047986", "88123048023", "88123048249", "88123048255", "88123048343", "88123048467",
           "88123048565", "88123048594", "88123048255", "88123048343", "88123048467",
           "88123050062", "88123049421", "88123049429", "88123049432", "88123049433",
           "88123049491", "88123049500", "88123049517", "88123049522"]

a = set(phones1)
b = set(phones2)

result = a.intersection(b)
print(result)

'''9 task'''

dict1 = {
    'car': 'black',
    'mouse': 'black',
    'pen': 'red'
}

dict1['phone'] = 'red'
print(dict1)
print(dict1.keys())

dict2 = {k: v for k, v in dict1.items() if v != 'black'}
print(dict2)

print(dict1.items())
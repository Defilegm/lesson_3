# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

list_new = [round(random.randint(0,10)+(random.random()),2) for i in range(6)]

print(list_new)

def diff(list):
    max = list[0]%1*100 
    min = list[0]%1*100 
    for i in list:
        if i%1*100 > max:
            max = i%1*100 
        if i%1*100 < min:
            min = i%1*100 
    print(f'Max значение дробной части: {round(max)}')
    print(f'Min значение дробной части: {round(min)}')
    return round((max - min)/100,2)

print(f'разница между макс и мин значениями дробной части: {diff(list_new)}')

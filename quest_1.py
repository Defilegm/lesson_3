# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

list_gen = [ random.randint(1,6) for i in range(10)]

print(list_gen)

def odd_summ(list):
    summ = 0
    for i in range(1,len(list),2):
        summ += list[i]
    return summ
print(odd_summ(list_gen))


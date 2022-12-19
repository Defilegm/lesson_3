# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

list_gen = [random.randint(1,5) for i in range(5)]

print(list_gen)

def multiply(lst):
    if len(lst)%2 > 0:
        lst[int(len(lst)/2)] *= lst[int(len(lst)/2)]
    for i in range(0,int(len(lst)/2)):
        lst[i] = lst[i]*lst[-1]
        lst.pop(-1)   
    return lst

print(multiply(list_gen))
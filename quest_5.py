# ; Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# ; Пример:

# ; - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]



def f(n):
    list=[0,1]
    list1=[]
    for i in range(n):
        list.append(list[i] + list[i+1])
    for i in range(n+1):
        list1.append((-1)**(i+2)*(list[i+1]))
    list1.reverse()
    list1.extend(list)
    return list1

print(f(8))




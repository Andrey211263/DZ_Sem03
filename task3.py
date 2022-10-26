# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:  - [1.1, 1.2, 3.1, 5, 10.01] => 0.2
import random
random.random()

number = int(input('Задайте длину списка '))
lst = []
for i in range(number):
    lst.append(round(random.uniform(1, 10), 3))
print(lst)
min = round(lst[0] % 1, 3)
max = round(lst[1] % 1, 3)
for i in range(0, number):
    res = round(lst[i] % 1, 3)
    # print(f'min={min}, max={max}, res={res}')
    if res < min:
        min = res
    elif res > max:
        max = res
print()    
print(f'max = {max} min = {min}, разница = {max - min}  ') 

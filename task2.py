# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:   - [2, 3, 4, 5, 6] => [12, 15, 16];
#           - [2, 3, 5, 6] => [12, 15]

from random import randint


number = int(input('Задайте длину списка '))
lst = []
for i in range(number):
    lst.append(randint(1, 10))
print(lst)
work = []
i = 0
count = number - 1
# for i in range(i, number):
while i < count:
    work.append(lst[i] * lst[count])
    # print(f'Произведение, i={i}, -> {lst[i]},*{lst[count]}  = {work[i]}')
    i += 1 
    count -= 1
if number % 2 != 0:
    work.append(lst[i] * lst[i])
print(work)

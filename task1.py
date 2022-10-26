# задайте список из нескольких чисел. напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции. пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from random import randint


number = int(input('Задайте длину списка '))
lst = []
for i in range(number):
    lst.append(randint(1, 999))
print(lst)
summ = 0
for i in range(0, number, 2):
    summ += lst[i]
    # print(f'Нечетная позиция, i = {i}, = {lst[i]}')
print('Искомая сумма =', summ)

# exit()

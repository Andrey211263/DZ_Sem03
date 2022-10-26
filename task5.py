# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

number = int(input('Задайте число '))
lst = []
nonlst = []

for i in range(0, number + 1):
    if i == 0:
        lst.append(0)
    elif i == 1:
        lst.append(1)
    else:
        lst.append(lst[i-1] + lst[i-2])
for i in range(number, 0, -1):
    nonlst.append(((-1)**(i+1)) * lst[i])
# print(lst)
# print()
# print(nonlst)
print('K = ', number, end = ' --> ')
print(nonlst + lst)


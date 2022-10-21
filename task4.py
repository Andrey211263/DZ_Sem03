# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: # - 45 -> 101101
#           - 3 -> 11
#           - 2 -> 10

number = int(input('Введите число '))
res = number
lst = []
while res != 0:
    lst.append(res % 2)
    res //= 2
# print(*lst) 
result = []
count = len(lst) - 1
i = 0
while count >= i:
    # print(f'i = {i}, count-i = {count - i},  элементы списка {lst[count - i]}')
    result.append(lst[count - i])
    i += 1
print(number, ' ->',*result)    

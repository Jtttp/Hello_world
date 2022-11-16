import math

# Завдання 1

lst = [65, 98, -1, 76, 897, 12, 435, -42, 234, -323, 106, 2]
print(lst)
print('Найбільший елемент списку: ', max(lst))
print('Найменший елемент списку: ', min(lst))
print('Сума чисел: ', sum(lst))
avr = sum(lst) / len(lst)
print('Середнє значення списку: ', avr)

# Завдання 2

list1 = list()
nums1 = int(input('Введіть кількість чисел першого списку: '))
for i in range(nums1):
    num1 = int(input('Введіть число: '))
    list1.append(num1)

list2 = list()
nums2 = int(input('Введіть кількість чисел другого списку: '))
for i in range(nums2):
    num2 = int(input('Введіть число: '))
    list2.append(num2)

list1.extend(list2)
print('Список з введених вами чисел:\n', list1)
my_set = set(list1)
new_list = list(my_set)
unq_list = []
for i in new_list:
    unq_list.append(i)
print('Унікальні значення списку\n', unq_list)

unq_list.reverse()
print('Список у зворотній послідовності:\n', unq_list)
print('Сортування списку за зростанням:\n', sorted(unq_list))
print('Сортування списку за спаданням:\n', sorted(unq_list)[::-1])

# Завдання 3

x = 0
y = 0
while y <= x:
    print('Задайте діапазон чисел')
    x = int(input('Введіть ціле число: '))
    y = int(input('Введіть ціле число більше за попереднє: '))
    if y <= x:
        print('Задайте коректний діапазон')
num_list = []
for b in range(x, y):
    d = 2
    while b % d != 0:
        d += 1
    if d == b:
        num_list.append(b)
print('Прості числа у даному діапазоні:', num_list)
print('''\nМеню:
\n1. Підрахунок суми простих чисел діапазону\n2. Підрахунок добутку простих чисел діапазону\n3. Вихід''')
choice = int(input('Ваш вибір: ', ))
if choice == 1:
    print('Сума:', sum(num_list))
elif choice == 2:
    print('Добуток:', math.prod(num_list))
elif choice == 3:
    print('Вихід')
else:
    print('Оберіть один із запропонованих варіантів')

# Завдання 4

my_list = [87, -3, 62, 104, -48, 20, 0, 73, -49, 5, 28]
print('Дано список:', my_list)
print('''\nМеню:
\n1. Виведення даних значень у зворотньому порядку\n2. Виведення даних значень за зростанням\n3. Вихід\n''')

choice = int(input('Ваш вибір: ', ))
if choice == 1:
    my_list.reverse()
    print(my_list)
elif choice == 2:
    my_list.sort()
    print(my_list)
elif choice == 3:
    print('Вихід')
else:
    print("Оберіть один із запропонованих варіантів")

# Завдання 5

int_list = [7, 4, -2, 13, 28, 8, 122, 87, -36, 0, 52, 34, 67, 9, -13, 5, 64, -61, 9, -23, 48, 90, -25, 118, 31, 2]
print('Список натуральних чисел:\n', int_list)
new_list = int_list[0::2]
print('Список непарних значень списку:\n', new_list)
repeat = int(input('Введіть кількість повторів для попереднього списку: ', ))
if repeat <= 0:
    print('Введіть коректне значення')
else:
    print('Дублювання списку на', repeat, 'повторів:\n', new_list * repeat)
int_list.clear()

# Завдання 6

print('Список натуральних чисел:\n', new_list)
num = int(input('Введіть значення для виявлення повторів у списку: ', ))
if num in new_list:
    print('Введене вами число', num, 'входить до списку')
    print('Кількість повторів числа', num, 'в списку:', new_list.count(num))
    print('Позиція введеного вами числа', num, 'в списку:', new_list.index(num))
else:
    print('Введене вами число', num, 'не входить до списку')

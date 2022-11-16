# import math
#
# print('''Меню:\n1. Додавання\n2. Віднімання\n3. Множення\n4. Ділення\n5. Косинус\n7. Синус\n8. Тангенс\n9. Вихід\n''')
#
# choice = input('Введіть номер обраної операції: ', )
#
#
# if choice == 1:
#     a = int(input('Введіть перше число: ', ))
#     b = int(input('Введіть друге число: ', ))
#     print('Сума: ', sum(a, b))
# else choice == 2:
#     a = int(input('Введіть перше число: ', ))
#     b = int(input('Введіть друге число: ', ))


#else choice == 2:
 #   def _numbers(a, b):
   #     return a - b
#
 #   x = add_numbers(a, b)
   # print('Сума даних чисел: ', x)



# def rec_sum(x, y):
#     if x == y:
#         return x
#     else:
#         return y + rec_sum(x, y - 1)
#
#
# num_1 = int(input('Введіть менше число для визначення діапазону: '))
# num_2 = int(input('Введіть менше число для визначення діапазону: '))
# print(rec_sum(num_1, num_2))

step_0 = 1
step_1 = 1
N = int(input("Число: "))
if N < 2:
    print(1)
else:
    for i in range(2, N + 1):
        s_n = step_0 + step_1
        step_0 = step_1
        step_1 = s_n
    print(i, s_n)




















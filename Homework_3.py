# Завдання 1

name = input("What is your name? ")
if name == "Julia":
    print('Really? Me too!')
else:
    print('Nice to meet you,', name,'!')


# Завдання 2

import math
x = float(input('Для обчислення значення функції y=cos(3x), введіть значення x, що задовольняє умову -𝜋 <= x <= 𝜋: '))
if -math.pi <= x <= math.pi:
    y = math.cos(3 * x)
    print('cos(3x) = ', y)
else:
    print("Введене вами число не задовольняє виконання умови -𝜋 <= x <= 𝜋")


# Завдання 3
import math

print('Введіть коефіцієнти a, b, c:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
d = b ** 2 - 4 * a * c
if d < 0:
    print('Дійсних коренів немає')
elif d > 0:
    x1 = (-b + (d ** 0.5 )) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)
    print('x1 = ', x1)
    print('x2 = ', x2)
elif d == 0:
    x = -b / (2 * a)
    print('x = ', x)
else:
    print('Невірно вказаний формат')


# Завдання 4

import math

print('''\nМеню:
\n1. Додавання\n2. Віднімання\n3. Множення\n4. Ділення\n5. Зведення в ступінь\n6. Квадратний корінь\n7. Кубічний корінь\n8. Синус числа\n9. Косинус числа\n10. Тангенс числа\n
''')

choice = int(input('Ваш вибір: '))

if choice == 1:
    x = float(input("Введіть число: "))
    y = float(input("Введіть число: "))
    addition = x + y
    print('Результат додавання: ', addition)
elif choice == 2:
    x = float(input("Введіть число: "))
    y = float(input("Введіть число: "))
    subtraction = x - y
    print('Результат віднімання: ', subtraction)
elif choice == 3:
    x = float(input("Введіть число: "))
    y = float(input("Введіть число: "))
    multipliction = x * y
    print('Результат множення: ', multipliction)
elif choice == 4:
    x = float(input("Введіть число: "))
    y = float(input("Введіть число: "))
    division = x / y
    if y == 0:
        print('Ділення на 0!')
    else:
        print('Результат ділення: ', division)
elif choice == 5:
    x = float(input("Введіть число: "))
    y = float(input("Введіть ступінь: "))
    squared = x ** y
    print('Результат зведення в ступінь: ', squared)
elif choice == 6:
    x = float(input("Введіть число: "))
    squere_root = x ** 0.5
    print('Результат: ', squere_root)
elif choice == 7:
    x = float(input("Введіть число: "))
    cube_root = x ** (1 / 3)
    print('Результат: ', cube_root)
elif choice == 8:
    x = float(input("Введіть число: "))
    sin = math.sin(x)
    print('Результат: ', sin)
elif choice == 8:
    x = float(input("Введіть число: "))
    sin = math.sin(x)
    print('Результат: ', sin)
elif choice == 9:
    x = float(input("Введіть число: "))
    cos = math.cos(x)
    print('Результат: ', cos)
elif choice == 10:
    x = float(input("Введіть число: "))
    tan = math.tan(x)
    print('Результат: ', tan)
else:
    print("Оберіть один із запропонованих варіантів")


# Завдання 5

number = int(input('''\nПеревірка числа на парність.\nВведіть число, яке хочете перевірити: '''))
print('Це парне число' if number % 2 == 0 else 'Це непарне число')


# Завдання 6

day = input("Введіть день тижня: ").lower()

match day:
    case 'понеділок':
        print('Сьогодні на роботу')
    case 'вівторок':
        print('Сьогодні на роботу')
    case 'середа':
        print('Сьогодні на роботу')
    case 'четвер':
        print('Сьогодні на роботу')
    case 'п"ятниця':
        print('Сьогодні на роботу')
    case 'субота':
        print('Сьогодні вихідний')
    case 'неділя':
        print('Сьогодні вихідний')
    case _:
        print('Такого дня не існує')


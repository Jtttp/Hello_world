# Завдання 3

# Створіть програму-калькулятор, яка підтримує наступні операції: додавання, віднімання, множення, ділення, зведення в
# ступінь, зведення до квадратного та кубічного коренів. Всі дані повинні вводитися в циклі, доки користувач не вкаже,
# що хоче завершити виконання програми. Кожна операція має бути реалізована у вигляді окремої функції. Функція ділення
# повинна перевіряти дані на коректність та видавати повідомлення про помилку у разі спроби поділу на нуль.

print("Калькулятор")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x):
    return x ** 2


def root_square(x):
    return x ** 0.5


def root_cube(x):
    return x ** (1 / 3)


while True:
    print('''\nМеню:\n
    1. Додавання
    2. Віднімання
    3. Множення
    4. Ділення
    5. Зведення в ступінь
    6. Корінь квадратний
    7. Корінь кубічний
    8. Вихід\n''')
    menu = int(input('Введіть номер обраної операції: ', ))
    if menu == 1:
        num_1 = int(input('Введіть перше число: '))
        num_2 = int(input('Введіть друге число: '))
        print('Результат додвання чисел = ', add(num_1, num_2))
    elif menu == 2:
        num_1 = int(input('Введіть перше число: '))
        num_2 = int(input('Введіть друге число: '))
        print('Результат віднімання чисел: ', subtract(num_1, num_2))
    elif menu == 3:
        num_1 = int(input('Введіть перше число: '))
        num_2 = int(input('Введіть друге число: '))
        print('Результат множення чисел: ', multiply(num_1, num_2))
    elif menu == 4:
        num_1 = int(input('Введіть перше число: '))
        num_2 = int(input('Введіть друге число: '))
        if num_2 == 0:
            print('Ділення на 0')
        else:
            print('Результат ділення чисел: ', divide(num_1, num_2))
    elif menu == 5:
        num_1 = int(input('Введіть число: '))
        print('Результат піднесення до квадрату: ', power(num_1))
    elif menu == 6:
        num_1 = int(input('Введіть число: '))
        print('Корінь квадратнний числа: ', root_square(num_1))
    elif menu == 7:
        num_1 = int(input('Введіть число: '))
        print('Корінь кубічний числа: ', root_cube(num_1))
    elif menu == 8:
        print('Вихід')
        break
    else:
        print('Оберіть один із запропонованих варіантів меню')
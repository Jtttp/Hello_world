# Завдання 3

print("Калькулятор")


def add(x, y):
    """Функція add виводить суму введених користувачем чисел"""
    return x + y


def subtract(x, y):
    """Функція subtract виводить різницю введених користувачем чисел"""
    return x - y


def multiply(x, y):
    """Функція multiply виводить добуток введених користувачем чисел"""
    return x * y


def divide(x, y):
    """Функція divide виводить частку введених користувачем чисел"""
    return x / y


def power(x):
    """Функція power підносить до квадрату введене користувачем число"""
    return x ** 2


def root_square(x):
    """Функція root_square виводить корінь квадратний введеного користувачем числа"""
    return x ** 0.5


def root_cube(x):
    """Функція root_cube виводить корінь кубічний введеного користувачем числа"""
    return x ** (1 / 3)


while True:
    print('''
    Меню:
    1. Додавання
    2. Віднімання
    3. Множення
    4. Ділення
    5. Зведення в ступінь
    6. Корінь квадратний
    7. Корінь кубічний
    8. Вихід
    ''')
    menu = int(input('Введіть номер обраної операції: ', ))
    if menu == 1:
        num_1 = int(input('Введіть перше число: '))
        num_2 = int(input('Введіть друге число: '))
        print(f'Результат додавання чисел: {add(num_1, num_2)}')
    elif menu == 2:
        num_1 = int(input('Введіть перше число: '))
        num_2 = int(input('Введіть друге число: '))
        print(f'Результат віднімання чисел: {subtract(num_1, num_2)}')
    elif menu == 3:
        num_1 = int(input('Введіть перше число: '))
        num_2 = int(input('Введіть друге число: '))
        print(f'Результат множення чисел: {multiply(num_1, num_2)}')
    elif menu == 4:
        num_1 = int(input('Введіть перше число: '))
        num_2 = int(input('Введіть друге число: '))
        if num_2 == 0:
            print('Ділення на 0')
        else:
            print(f'Результат ділення чисел: {divide(num_1, num_2)}')
    elif menu == 5:
        num_1 = int(input('Введіть число: '))
        print(f'Результат піднесення до квадрату: {power(num_1)}')
    elif menu == 6:
        num_1 = int(input('Введіть число: '))
        print(f'Корінь квадратнний числа: {root_square(num_1)}')
    elif menu == 7:
        num_1 = int(input('Введіть число: '))
        print(f'Корінь кубічний числа: {root_cube(num_1)}')
    elif menu == 8:
        print('Вихід')
        break
    else:
        print('Оберіть один із запропонованих варіантів меню')

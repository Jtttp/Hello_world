# Завдання 5
#
# Створіть функцію quadratic_equation, яка приймає на вхід 3 параметри: a, b, c. Усередині цієї функції створити змінні
# x1, x2 зі значенням None (спочатку приймаємо, що рівняння не має коренів) та функцію calc_rezult з формальними
# параметрами зовнішньої функції quadratic_equation. Всередині функції calc_rezult здійснити пошук дискримінанта,
# згідно з результатом якого зробити розрахунок коренів рівняння. Зовнішня функція quadratic_equation має повернути
# перелік значень коренів квадратного рівняння. Надати можливість користувачеві ввести з клавіатури формальні параметри
# для передачі їх у створену функцію quadratic_equation, результати роботи функції відобразити на екрані.

def quadratic_equation(a, b, c):
    x_1, x_2 = None, None
    def calc_rezult(a, b, c):
        discriminant = (b ** 2) - (4 * a * c)
        nonlocal x_1
        nonlocal x_2
        if discriminant > 0:
            x_1 = (-b - (discriminant ** 0.5)) / (2 * a)
            x_2 = (-b + (discriminant ** 0.5)) / (2 * a)
        elif discriminant == 0:
            x_1 = -b / (2 * a)
            x_2 = x_1


def calc_rezult(a, b, c):
    if x_1 is None:
        return 'Дискримінант менше нуля. Коренів немає'
    else:
        return f'x_1 = {x_1:.3f} \nx_2 = {x_2:.3f}'

def main():
    while True:
        try:
            x = float(input('a = '))
            y = float(input('b = '))
            z = float(input('c = '))
            break
        except ValueError:
            print('Введіть коректне значення')

    print(quadratic_equation(a=x, b=y, c=z))

main()

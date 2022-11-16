# Завдання 6

# Створіть прототип програми «Бібліотека», де є можливість перегляду та внесення змін за структурою: автор: твір.
# Передбачте можливість виведення на екран сортування за автором та твором.
from collections import OrderedDict
print('Бібліотека')

dict_library = {"Нечуй-Левицький Іван": "Кайдашева сім'я", "Вороний Микола": "Блакитна Панна",
                "Котляревський Іван": "Енеїда", "Симоненко Василь": "Задивляюсь у твої зіниці",
                "Олесь Олександр": "Чари ночі", "Рутківський Володимир": "Джури козака Швайки",
                "Мирний Панас": "Хіба ревуть воли, як ясла повні?", "Українка Леся": "Contra spem spero!",
                "Коцюбинський Михайло": "Intermezzo"}
print('Каталог:')
print(dict_library)
print('''\nМеню:\n1. Додати книгу до каталогу\n2. Сортування за автором\n3. Сортування за назвою книги\n4. Вихід''')
choice = int(input('Ваш вибір: ', ))

if choice == 1:
    add_writter = str(input("Введіть призвіще та ім'я письменника: ", ))
    add_book = str(input("Введіть назву книги: ", ))
    dict_library.update({add_writter: add_book})
    print('Книгу додано до каталогу:', dict_library)
elif choice == 2:
    print('Сортування за автором:')
    dict_key_sorted = OrderedDict(sorted(dict_library.items()))
    print(dict_key_sorted)
elif choice == 3:
    print('Сортування за назвою книги:')
    dict_value_sorted = {key: value for key, value in sorted(dict_library.items(),
                                                             key=lambda item: item[1])}
    print(dict_value_sorted)
elif choice == 4:
    print('Вихід')
else:
    print('Оберіть один із запропонованих варіантів')

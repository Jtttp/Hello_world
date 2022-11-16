# Завдання 2
#
# Створіть програму, яка перевіряє, чи є паліндромом введена фраза.

"""Дана функція визначає чи є слово або фраза паліндромом"""


def palindrom(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrom(word[1:-1])


your_word = str(input('Введіть фразу для перевірки на паліндром: ', ))
print(palindrom(your_word))

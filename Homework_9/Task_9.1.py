# Завдання 1

# Прочитайте у документації з мови Python інформацію про перелічені у резюме цього уроку стандартні функції. Перевірте
# їх на практиці.

words = ("Welcome", "to", "Python")
print(words)
print(*words, end="!\n")
print(*words, sep="\n")

print(len(words))

number = 1000
number_str = str(number)
print(type(number_str))
print(number_str)

number_str = "1000"
number_int = int(number_str)
print(type(number_int))
print(number_int)

number_float = float(number_int)
print(type(number_float))
print(number_float)

word = "Hello, word"
new_list = list(word)
print(new_list)

list_to_set = set(new_list)
print(list_to_set)

str_to_tuple = tuple("Hello")
list_to_tuple = tuple([1, 2, 3, 4, 5])
print(str_to_tuple)
print(list_to_tuple)

list_of_tuples = list(zip(str_to_tuple, list_to_tuple))
print(list_of_tuples)

new_dict = dict(list_of_tuples)
print(new_dict)

print(bool(1))
print(bool(0))

print(len(new_dict))

print(sum(list_to_tuple))

print(min(list_to_tuple))

range(1000)
print(range(1000))

numbers = [2, 1, 3, 4, 7]
print(reversed(numbers))

numbers = [1, 8, 2, 13, 5, 3, 1]
print(sorted(numbers, reverse=True))

print(issubclass(int, bool))
print(issubclass(bool, int))

print(isinstance(True, bool))
print(isinstance(True, str))

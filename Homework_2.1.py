# Завдання 1

country = input("Введіть країну вашого народження: ")
city = input("Введіть місто вашого народження: ")
print("Ви народилися в " + city + ", " + country)

# Завдання 2
a = int(input("Введіть ціле число "))
b = int(input("Введіть ціле число "))
x = int(input("Введіть ціле число "))
c = str(a * b * x)
print("Добуток введених вами чисел складає: " + c)

# Завдання 3
a = int(input("Введіть число "))
b = int(input("Введіть число "))
c = int(input("Введіть число "))
x = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 / a
print(x)

# Завдання 4
f = input("Введіть текст: ")
print("Тексту відповідає ASCII значення '" + f + "' is ", ord(f))

# Завдання 5
string = input("Введіть текст ")[::-1]
print(string)

# Завдання 6
r = int(input("Введіть радіус круга "))
import math

S = math.pi * r ** 2
print("Площа круга дорівнює " + str(S))

# Завдання 7
lenghth = 700
velocity = 90
time = lenghth / velocity
print(time)

# Завдання 8
name = input("Enter your name ")
age = input("Enter your age ")
print("My name is " + name + " and I am " + str(age))

# Завдання 2

# Створіть програму, яка емулює роботу сервісу зі скорочення посилань. Повинна бути реалізована можливість введення
# початкового посилання та короткої назви і отримання початкового посилання за її назвою.

top_ukr_youtubers = {
    'cutt.ly/9NGMjoK': 'youtube.com/channel/UCpgNxHZ3TCbB3_Xczm9TIDg',
    'cutt.ly/pNGM1D3': 'youtube.com/channel/UC1Xz2zFyRGvt06qMJHfz27w',
    'cutt.ly/kNG1b3a': 'youtube.com/channel/UCdlfo5folV5oO5WsPgSE_Cw',
    'cutt.ly/mNG1JZP': 'youtube.com/channel/UCNfxB3nWgDIpkItC6KSqKsw',
    'cutt.ly/VNG15so': 'youtube.com/channel/UCRyR18PmBT1WFEHUmttlEpQ'
}

print('Рейтинг україномовного YouTube\n')

print('1. Чоткий Паца')
print('2. Діма і машинки')
print('3. Afinka')
print('4. Riddle UA')
print('5. Стася Мар')

print('Для отримання повного посилання на сторінку блогера''')

name = str(input('\nВведіть ім\'я блогера: '))
if name == 'Чоткий Паца':
    print(top_ukr_youtubers['cutt.ly/9NGMjoK'])
elif name == 'Діма і машинки':
    print(top_ukr_youtubers['cutt.ly/kNG1b3a'])
elif name == 'Afinka':
    print(top_ukr_youtubers['cutt.ly/kNG1b3a'])
elif name == 'Riddle UA':
    print(top_ukr_youtubers['cutt.ly/mNG1JZP'])
elif name == 'Стася Мар':
    print(top_ukr_youtubers['cutt.ly/VNG15so'])
else:
    print('Такого імені не існує. Введіть коректне значення')

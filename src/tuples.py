#!/usr/bin/python3

# Создаем некоторый список со значениями
some_list = ['Привет', 'мир', '!']

# Создадим некоторый словарь со значениями
some_dict = {'Имя': 'Анна', 'Возраст': 21, 'Пол': 'Женский'}

# Создадим некоторый кортеж со значениями
some_tuple = (1, 'слово', 80)

# Выведем значения списка
for item in some_list:
    print(item)

# Выведем значения словаря
for item in some_dict:
    print(item)

# Выведем значения кортежа
for item in some_tuple:
    print(item)

# Выведем все ключи словаря
for item in some_dict.keys():
    print(item)

# Выведем все значения словаря
for item in some_dict.values():
    print(item)

# Получим содержимое словаря
for item_key, item_value in some_dict.items():
    print(f'{item_key}: {item_value}')

# Выводим значения списка с помощью счетчика и цикла while
counter = 0

while counter < len(some_list):
    print(some_list[counter])
    counter = counter + 1

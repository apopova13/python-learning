#!/usr/bin/python3

# Запись в файл контекстным менеджером
with open('some.txt', 'w') as file:
    file.write('Привет мир')

# Чтение из файла с помощью контекстного менеджера
with open('some.txt', 'r') as file:
    print(file.read())

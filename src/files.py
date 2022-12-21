#!/usr/bin/python3

# Открытие для записи файла и запись
file = open('some.txt', 'w')
file.write('Привет мир\n')
file.close()

# Открытие для дозаписи файла и запись в файл
file = open('some.txt', 'a')
file.write('Новая строка\n')
file.close()

# Открытие для чтения файла и чтение в data содержимого
file.open('some.txt', 'r')
data = file.read()
file.close()

# Вывод содержимого на экран
print(data)

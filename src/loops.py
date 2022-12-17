#!/usr/bin/python3

i = 0

# Цикл while
while i < 10:
    print(i)
    i = i + 1

a = 'Привет'

# Цикл for
for i in a:
    print(i)

# Вывод циклом for буквы вместе с индексом
for index, letter in enumerate(a):
    print(f'{index}: {letter}')

i = 0

# Прерывание цикла с помощью break
while i < 10:
    if i == 5:
        break

    print(i)
    i = i + 1

# Прерывание цикла с помощью continue
while i < 10:
    i = i + i
    if i == 5:
        continue

    print(i)

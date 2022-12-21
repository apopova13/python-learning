#!/usr/bin/python3

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

# Результат в переменной z
try:
    z = x / y
except ZeroDivisionError:
    z = 0

print(f'z = {z}')

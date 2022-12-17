#!/usr/bin/python3

def get_max(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

def get_number():
    return int(input('Введите число: '))

x = get_number()
y = get_number()

max = get_max(x, y)

print(f'Из двух чисел {max} больше всех')

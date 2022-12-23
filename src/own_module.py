#!/usr/bin/python3

from lib.Calc import Calc

calc = Calc(5, 3)
print(f'Сумма чисел: {calc.get_sum()}')
print(f'Разность чисел: {calc.get_dif()}')
print(f'Произведение чисел: {calc.get_mul()}')
print(f'Частное из чисел: {calc.get_div()}')

#!/usr/bin/python3

a = list('Привет')
b = [1, 2, 3, 'б', 'q']

print(a)
print(b)

# Методы списков
a.append('!')
a.remove('!')
a.insert(3, ' ')
a.pop(1)
a.reverse()
a.sort()
a.clear()

# Пример функции len()
a = 'Привет'
b = [1, 2, 3]

print(len(a))
print(len(b))

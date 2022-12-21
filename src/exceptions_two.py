#!/usr/bin/python3

try:
    file = open('some.txt', 'r')
    data = file.read()
    file.close()
except FileNotFoundError:
    data = ''

print(data)

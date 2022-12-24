#!/usr/bin/python3

from Animal import Animal

class Cat(Animal):
    def __init__(self, gender):
        super().__init__(4, gender)

    def meow(self):
        print('Meow!')

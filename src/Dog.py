#!/usr/bin/python3

from Animal import Animal

class Dog(Animal):
    def __init__(self, gender):
        super().__init__(4, gender)
    
    def bark(self):
        print('Bark!')


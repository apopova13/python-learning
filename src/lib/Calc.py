#!/usr/bin/python3

class Calc:
    def __init__(self, first_number = 0, second_number = 0):
        self.first_number = first_number
        self.second_number = second_number

    def get_sum(self):
        return self.first_number + self.second_number

    def get_dif(self):
        return self.first_number - self.second_number

    def get_mul(self):
        return self.first_number * self.second_number

    def get_div(self):
        return self.first_number / self.second_number

    def get_first_number(self):
        return self.first_number

    def get_second_number(self):
        return self.second_number

    def set_first_number(self, number_value):
        self.first_number = number_value

    def set_second_number(self, number_value):
        self.second_number = number_value

import sys 

def decimal_to_base60(decimal_num):
    """Converts a decimal number to base 60."""

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx"
    result = ""
    while decimal_num > 0:
        result = digits[decimal_num % 60] + result
        decimal_num //= 60
    return result

def base60_to_decimal(base60_num):
    """Converts a base 60 number to decimal."""

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx"
    result = 0
    power = 1
    for digit in reversed(base60_num):
        result += digits.index(digit) * power
        power *= 60
    return result

def decimal_to_cuneiform(decimal_number):
    if decimal_number == 0:
        return '-'
    
    cuneiform_numerals = {
        1: '|',  # Vertical wedge
        10: '<',  # Horizontal wedge
        # Add more cuneiform numerals as needed
    }
    cuneiform_number = ''
    for numeral in sorted(cuneiform_numerals.keys(),
                          reverse=True):
        while decimal_number >= numeral:
            cuneiform_number += cuneiform_numerals[numeral]
            decimal_number -= numeral
    return cuneiform_number

class Base60:
    """Base 60 number and associate functions"""
    def __init__(self, n):
        if type(n) == int:
            self.b10 = n
            self.b60 = decimal_to_base60(n)
        elif type(n) == str:
            self.b60 = n
            self.b10 = base60_to_decimal(n)
        else:
            raise TypeError("Only int or base60 format string allowed.")
    
    def __str__(self):
        return self.b60

    def __repr__(self):
        return self.b60
    
    def __add__(self, other):
        if type(other) == int:
            num = (self.b10 + other)
        else:
            num = self.b10 + base60_to_decimal(other)
        return Base60(num)
    
    def __sub__(self, other):
        if type(other) == int:
            num = (self.b10 - other)
        else:
            num = self.b10 - base60_to_decimal(other)
        return Base60(num)
    
    def __mul__(self, other):
        if type(other) == int:
            num = (self.b10 * other)
        else:
            num = self.b10 * base60_to_decimal(other)
        return Base60(num)
    
    def __pow__(self, other):
        if type(other) == int:
            num = (self.b10 ** other)
        else:
            num = self.b10 ** base60_to_decimal(other)
        return Base60(num)
    def __truediv__(self, other):
        raise TypeError("__truediv__ '/' is not allowed in Base60. Please use __floordiv__ '//' or __mod__ '%'.")
    

    def __floordiv__(self, other):
        if type(other) == int:
            num = (self.b10 // other)
        else:
            num = self.b10 // base60_to_decimal(other)
        return Base60(num)
    
    def __mod__(self, other):
        if type(other) == int:
            num = (self.b10 % other)
        else:
            num = self.b10 % base60_to_decimal(other)
        return Base60(num)

    def __reversed__(self):
        return self.b60
    
    """ Convert to cuneiform """
    def cuneiform(self):
        output = ""
        for digit in self.b60:
            output += f" {decimal_to_cuneiform(base60_to_decimal(digit))}"
        return output
    



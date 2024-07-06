'''
EXERCISE 1:
The exercise here is to write a dictionary in the most efficient way possible.
we have an enum and we should write a dictionary that maps the enum to a function.
'''

from enum import Enum

class MyEnum(Enum):
    A = 1
    B = 2
    C = 3
    D = 4

def func_a():
    return "A"

def func_b():
    return "B"

def func_c():
    return "C"

def func_d():
    return "D"

def get_func(enum):
    # Go to MyEnum and place the cursor before A,
    # then double-click on OPT key and hold it, press down arrow to select all the enum values,
    # shift + right arrow to select the values
    # CMD + C to copy the values
    # go to enum_functions
    # write `MyEnum: func_`
    # click CMD + D 3 times, the row `MyEnum: func_,` shall be duplicate for 4 times
    # select MyEnum ang click CMD + G for 3 times (the expression `MyEnum` shall be selected)
    # click right arrow to put the cursor after `MyEnum`, click on "." and paste the values
    # click on OPT (and hold it) + right arrow 2 times to go before the comma
    # click CMD + V to paste the values
    # shift + left arrow to select the values (letters in uppercase)
    # click CMD + U to make the letters lowercase
    enum_functions = {

    }

    return enum_functions.get(enum)

'''
EXERCISE 2:
The exercise here is to write a dictionary in the most efficient way possible.
we have a class with its attributes and we should write a dictionary that maps the attributes to their uppercase names.
'''
class OtherClass:
    def __init__(self, value):
        self.value = value

class MyClass:
    def __init__(self):
        self.a = OtherClass("A")
        self.b = OtherClass("B")
        self.c = OtherClass("C")
        self.d = OtherClass("D")

    def get_dict(self):
        # Expected result: {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
        # hint: use the expression `"": self..value,`
        attributes = {}

        return attributes

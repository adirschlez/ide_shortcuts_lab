'''
EXERCISE 1:
Navigate to the declaration of the `func_a` function using CMD + B.
EXERCISE 2:
Navigate to the declaration of the `result` function using CMD + B.
'''

def func_a():
    return 4


def rec_func_a(value):
    if value == 0:
        return func_a()
    return rec_func_a(value - 1)

def process_data():
    result = func_a()

    result += 2

    while result < 10:
        result += 1
        print(result)

    return result
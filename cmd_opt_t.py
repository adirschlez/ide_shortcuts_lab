"""
EXERCISE 1:
Surround the block of code with an `if` statement using Option + Command + T.
"""

def process_data(data):
    result = None
    # Surround this block with an `if` statement
    result = data * 2
    return result



"""
EXERCISE 2:
Surround the block of code with an `if` statement using Option + Command + T.
"""
def iterate_data(data_list):
    results = []

    # Surround this block with a `while` loop
    data = data_list.pop()
    print(f"Processing data: {data}")
    results.append(data)

    return results


"""
EXERCISE 3:
Surround the block of code with an `if` statement using Option + Command + T.
"""
def handle_exceptions(data):
    result = None

    # Surround this block with a `try-except` block
    result = 10 / data

    return result
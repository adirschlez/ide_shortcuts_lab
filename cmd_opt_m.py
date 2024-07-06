'''
EXERCISE 1:
Refactor the code block in the `process_data` function by extracting it into a separate method using CMD + OPT + M.
'''

def process_data(data):
    result = None

    # Extract this block into a separate method called my_business_logic
    result = data ** 2

    return result


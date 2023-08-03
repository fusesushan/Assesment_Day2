'''Create a function convert_to_uppercase that takes a list of strings as input
and uses the map function to return a new list with all the strings converted to
uppercase.
'''
def square_numbers(input_list):
    squared_list = list(map(lambda x: x**2, input_list))
    return squared_list

# Test the function
numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers)
print(squared_numbers)

''' Implement a function called filter_prime_numbers that takes a list of
integers as input and uses the filter function to return a new list containing only the
prime numbers.'''
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime_numbers(numbers):
    return list(filter(is_prime, numbers))

input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime_numbers(input_numbers)
print(prime_numbers)

'''Write a Python function calculate_factorial that takes an integer as input
and uses the reduce function to return the factorial of that number.
'''
from functools import reduce
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for neg num")
    if n == 0 or n == 1:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))

num = 5
factorial = calculate_factorial(num)
print(f"The factorial of {num} is {factorial}")

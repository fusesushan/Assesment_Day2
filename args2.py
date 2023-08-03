'''
[*args] Write a Python function that takes an arbitrary number of positional
arguments and returns the sum of all the numbers. Test your function with various
input cases.

'''
def sum_all(*num):
    '''Function that takes an arbitrary number of positional arguments and
    returns the sum of all the numbers'''
    sum = 0
    for i in num:
        sum = sum + i
    return(sum)

def sum_all_v2(*args):
    '''Function that takes an arbitrary number of positional arguments and
    returns the sum of all the numbers using sum'''
    total = sum(args)
    return total

print(sum_all_v2.__doc__)
print(sum_all_v2(1, 2, 4, 6, 8, 9)) # Passing int nummbers
print(sum_all_v2(1.2, 3.4, 5.6, 7.9)) # Passing floating point numbers
print(int(sum_all_v2(1.2, 3.4, 5.6, 7.9))) # Typecasting result to int

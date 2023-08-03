''' [*args] Write a Python function concat_strings that takes any number of strings as
arguments and returns a single concatenated string.
'''
def concat_strings(*argv):
    result = ""
    for arg in argv:
        result = result+arg
    return(result)

print(concat_strings("I", " am", " concatinated", " with", " +"))

def concat_strings(*args):
    concatenated_string = ''.join(args)
    return concatenated_string

print(concat_strings("I", " am", " concatinated", " with", " join"))

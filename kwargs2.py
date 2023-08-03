'''
[**kwargs] Write a Python function calculate_total_cost that calculates the total
cost of items purchased from a store. The function should accept multiple keyword
arguments, where the key is the item name, and the value is the item's price. The
function should return the total cost of all items.
'''

def calculate_total_cost(**kwargs):
    '''function implementing kwargs tat gives total cost of items purchased'''
    price = 0
    for _, value in kwargs.items():
        price += value
    return price

print(calculate_total_cost.__doc__)
print(calculate_total_cost(potato=100, Dettol=560, Basmati=2790))

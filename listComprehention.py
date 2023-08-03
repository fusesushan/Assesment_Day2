'''Task 1: Filter Strings with More Than 5 Characters'''
input_strings = ["apple", "banana", "grape", "kiwi", "orange", "strawberry", "pear"]
filtered_strings = [s for s in input_strings if len(s) > 5]
print(filtered_strings)


'''Task 2: Element-wise Product of Two Lists'''
list1 = [2, 4, 6, 8, 10]
list2 = [3, 5, 7, 9, 11]
product_list = [x * y for x, y in zip(list1, list2)]
print(product_list)

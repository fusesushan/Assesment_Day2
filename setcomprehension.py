'''Task 1: Create a Set of Unique Even Numbers'''

numbers = [2, 5, 8, 4, 10, 7, 6, 3, 8, 2]
unique_even_set = {num for num in numbers if num % 2 == 0}
print(unique_even_set)


'''Task 2: Create a Set of Unique Characters from Words'''

words = ["apple", "banana", "cherry", "grape", "orange"]
unique_chars_set = {char for word in words for char in word}
print(unique_chars_set)

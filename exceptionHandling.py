'''Task1: Handling ZeroDivisionError:'''
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

'''Task2: Handling FileNotFoundError:'''
try:
    filename = input("Enter the filename: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("File contents:\n", content)
except FileNotFoundError:
    print("Error: File not found.")

'''Task3: Handling ValueError for integer conversion:'''
try:
    user_input = input("Enter an integer: ")
    num = int(user_input)
    print("You entered:", num)
except ValueError:
    print("Error: Invalid input. Please enter an integer.")


'''Handling both ValueError and ZeroDivisionError:'''
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

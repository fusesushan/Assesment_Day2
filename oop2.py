"""Build a Python class to represent a simple banking system. Create a class for a
BankAccount, and another for Customer. The BankAccount class should have a
constructor to initialize the account details (account number, balance, account type).
The Customer class should have a constructor to set the customer's details (name,
age, address) and create a BankAccount object for each customer. Implement a
destructor for both classes to display a message when objects are destroyed"""

class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not Enough funds")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: Rs.{self.balance:.2f}")

    def __del__(self):
        print(f"Account {self.account_number} has been closed.")


class Customer:
    def __init__(self, name, age, address, initial_balance, account_type):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = BankAccount(self.generate_account_number(), initial_balance, account_type)

    def generate_account_number(self):
        return hash(self.name + self.address) % 999999999

    def display_customer_info(self):
        print("Customer Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        self.bank_account.display_balance()

    def __del__(self):
        print(f"Customer {self.name}'s account has been closed.")


# Create a Customer and BankAccount
customer1 = Customer("Sushan", 24, "Hattiban", 300000, "Savings")
customer2 = Customer("Kanchan", 24, "Sankhamul", 500000, "Current")

# Display customer information
customer1.display_customer_info()
customer2.display_customer_info()

# Perform transactions
customer1.bank_account.deposit(15000)
customer1.bank_account.withdraw(20000)
customer2.bank_account.deposit(2500)
customer2.bank_account.withdraw(3000)

# Display updated balances
customer1.bank_account.display_balance()
customer2.bank_account.display_balance()

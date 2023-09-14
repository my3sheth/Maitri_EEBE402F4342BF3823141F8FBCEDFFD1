class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited {amount:.2f} into {self.__account_holder_name}'s account. \n")
        else:
            print("Invalid deposit amount. Please enter a positive amount. \n")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew {amount:.2f} from {self.__account_holder_name}'s account. \n")
        else:
            print("Invalid withdrawal amount or insufficient balance. \n")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: {self.__account_balance:.2f} \n")

#main
account1 = BankAccount("1234", "John", 1000)
account1.display_balance()
account1.deposit(500.0)
account1.display_balance()
account1.withdraw(300.0)
account1.display_balance()
account1.withdraw(900.0)
account1.display_balance()
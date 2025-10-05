class BankAccount:
    def __init__(self, initial_balancee=0):
        self.__account_balance = initial_balancee

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Add amount to withdraw")
            return False
        
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")
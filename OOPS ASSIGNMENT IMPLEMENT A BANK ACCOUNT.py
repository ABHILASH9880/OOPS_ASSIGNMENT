class BankAccount:
    def _init_(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")


# Example usage
account1 = BankAccount(123456789)
account1.deposit(1000)
account1.withdraw(500)
account1.get_balance()

class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance
        return self

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name} Balance: {self.account.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

alaa = User("Alaa", "alaa@email.com")
ahmad = User("Ahmad", "ahmad@email.com")

alaa.make_deposit(500).make_deposit(100).make_withdrawal(150).display_user_balance()

alaa.transfer_money(ahmad, 200)

alaa.display_user_balance()
ahmad.display_user_balance()
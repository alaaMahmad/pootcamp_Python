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
    

class RetirementAccount (BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self


print("\n--- Retirement Account Early Withdrawal Test ---")

# Create a retirement account starting with $500
retirement_acc = RetirementAccount(balance=500)
retirement_acc.withdraw(100,True).display_account_info()

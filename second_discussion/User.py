class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name} Balance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


alaa = User("Alaa", "alaa@email.com")
ahmad = User("Ahmad", "ahmad@email.com")
yazan = User("Yazan", "yazan@email.com")

alaa.make_deposit(500)
alaa.make_withdrawal(100)
alaa.display_user_balance()  

alaa.transfer_money(ahmad, 150)

yazan.make_deposit(300)

alaa.display_user_balance()   
ahmad.display_user_balance()  
yazan.display_user_balance()
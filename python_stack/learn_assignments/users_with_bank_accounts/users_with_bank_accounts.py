class BankAccount:
    def __init__(self, int_rate,):
        self.int_rate = int_rate 
        self.savings_balance = 0
        self.checking_balance = 0
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposit: ", self.checking_balance)
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        if self.balance < amount:
            print("Insufficient Funds: Charging a $5 fee.")
            self.balance -= amount +5
            print("Withdrawal: ", self.checking_balance)
        return self

    def info(self):
        print("Balance: ", self.checking_balance)
        return self

    def yield_int(self):
        self.balance += self.balance * self.int_rate
        print("Interest: ")
        return self

    def transfer(self, other_user, amount):  
        other_user.account += amount
        print("Transfer: ", self.checking_balance)
        return self

class user:
    def __init__(self, name, email_address,):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate = 0.01)

    def make_deposit(self, account_type, amount):
        if account_type == "checking":
            self.account.checking_balance += amount
            print("user", self.name, "checking: ", self.account.checking_balance)
        if account_type == "savings":
            self.account.savings_balance += amount
            print("user", self.name, "savings: ", self.account.savings_balance)
        return self

    def make_withdrawal(self, account_type, amount):
        if account_type == "checking":
            self.account.checking_balance -= amount
            print("user", self.name, "checking: ", self.account.checking_balance)
        if account_type == "savings":
            self.account.savings_balance -= amount
            print("user", self.name, "savings: ", self.account.savings_balance)
        return self

    def display_balance(self):
        print("user: ", self.name,"checking: ", self.account.checking_balance, "savings: ", self.account.savings_balance)

    def make_transfer(self, other_user, account_type, amount):
        if account_type == "checking":
            self.account.checking_balance += amount
            print("user: ", self.name, "checking: ", self.account.checking_balance)
        if account_type == "savings":
            self.account.savings_balance += amount
            print("user: ", self.name, "saving: ", self.account.savings_balance)
        other_user.account.checking_balance += amount
        return self



guido = user("Guido van Rossum", "guido@python.com")
monty = user("Monty Python", "monty@python.com")
michael = user("Michael Dojo", "michael@codingdojo.com")
anna = user("Anna Dojo", "anna@codingdojo.com")
judge = user("Judge Fudge", "judge.smith@charter.net")

monty.display_balance().make_deposit("checking", 50)


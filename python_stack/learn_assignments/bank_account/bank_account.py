# 
# 

#  Bank Account:

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate 
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposit: ", self.balance)
        return self

    def withdrawal(self, amount):
        if self.balance > amount:
            self.balance -= amount
        if self.balance < amount:
            print("Insufficient Funds: Charging a $5 fee.")
            self.balance -= amount +5
            print("Withdrawal: ", self.balance)
        return self

    def display_account_info(self):
        print("Balance: ", self.balance)
        return self

    def yield_int(self):
        self.balance += self.balance * self.int_rate
        print("Interest: ")
        return self

    def transfer_money(self, other_user, amount):  
        other_user.account_balance += amount
        print("Transfer: ", self.balance)
        return self

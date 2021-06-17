# # 
# # 

# # User:If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance.

class user:
    def __init__(self, name, email_address,):     # method has two parameters.
        self.name = name         # use the values passed in to set the name attribute.
        self.email = email_address      # and the email attribute.
        self.account_balance = 0    # the account balance is set to $0 so no need for 3rd parameter.

    def make_deposit(self, amount):   # takes an argument that is the amount of the deposit.
        self.account_balance += amount # the specific user's account increases by the amount received.

    def make_withdrawal(self, amount):   # takes the argument that is the amount of the withdrawal.
        self.account_balance -= amount # the specific user's account decreases by the amount recieved.

    def display_balance(self):
        print(self)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

guido = user("Guido van Rossum", "guido@python.com")
monty = user("Monty Python", "monty@python.com")
michael = user("Michael Dojo", "michael@codingdojo.com")
anna = user("Anna Dojo", "anna@codingdojo.com")
judge = user("Judge Fudge", "judge.smith@charter.net")

print(guido.name)    # output
print(monty.name)    # output
print(michael.name)  # output
print(anna.name)     # output

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance) # output: 300
print(monty.account_balance) # output: 50

guido.display_balance()

guido.make_deposit(500)
guido.make_deposit(500)
guido.make_withdrawal(250)
guido.make_withdrawal(250)
guido.display_balance()

guido.transfer_money(monty, 50) 

### I now realize all of these 'calls' could have been chained. ###


guido.make_deposit(100).make_deposit(50).make_withdrawal(25).display_balance().transfer_money(judge,100)








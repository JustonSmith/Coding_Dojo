# 
# 
# Another kind of relationship between classes involves inheritance, which is defining a new class based on another class. In other words, it allows one class to take on the attributes and methods from another class with little additional code. This reuse of code results in reduced redundancy and complexity, which we as developers love! The derived classes (also referred to as child or sub classes) can override or extend the functionality of base classes (or parent or super classes).

# Let's consider our BankAccount class from the previous OOP chapter. What if we were told users could have both checking accounts and retirement accounts? There are a lot of things these two types of accounts have in common, but there are some attributes and methods that might differ between the two.

# One way to make a distinction between account types would be to add an attribute of account_type to our BankAccount class. Then in each of our methods, we would have a series of conditional statements that would determine how the method would actually run. But this can get pretty clunky and hard to manage.

# If we go to the other extreme and just create two separate classes, we might end up with something like this:

class CheckingAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        # code
    def withdraw(self, amount):
        # code
    def write_check(self, amount):
        # code
    def display_account_info(self):
        # code

    class RetirementAccount:
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.is_roth = is_roth
    def deposit(self, amount):
        # code - assess tax if necessary
    def withdraw(self, amount):
        # code - assess penalty if necessary
    def display_account_info(self):
        # code

# Still, this feels a little repetitive. Inheritance provides a balance between these two options--it allows us to have one parent class that holds the attributes and methods that are common between the new classes. In turn, each child class will only contain what is unique to that class:

class CheckingAccount(BankAccount):
    pass    

class RetirementAccount(BankAccount):
    pass

# Would you believe that (assuming the BankAccount class is complete) with just the inclusion of the parent class in parentheses, both the CheckingAccount and RetirementAccount classes both have all the attributes and functionality of the parent class? Amazing! Now we just need to figure out how to add the differences, while maintaining what we need from the parent class.

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.is_roth = is_roth  

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

# Do you see how the parent class already does 2 of the 3 lines we're trying to execute in our RetirementAccount class? Let's utilize the parent's functionality for this method. To indicate we are trying to use the parent's methods, we call on it with the keyword super. From there, we can call on any of the parent's methods:

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)	
        self.is_roth = is_roth	

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

# The first line in our RetirementAccount __init__ method allows the parent to manage the setting of int_rate and balance. The only line we need to add is to set the is_roth attribute, since this is unique to the RetirementAccount class.

# Let's look at another example. Suppose we wanted to add some logic to our withdraw method.

class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
    	    amount = amount * 1.10
        if (self.balance - amount) > 0:
        self.balance -= amount
        else:
        print("INSUFFICIENT FUNDS")
    return self

classcopy BankAccount:
    def withdraw(self, amount):
    if (self.balance - amount) > 0:
        self.balance -= amount
        else:
        print("INSUFFICIENT FUNDS")
    return self

# Hopefully you recognize the repetitiveness here and want to reduce it! So let's call on the parent to do the part of the code that is the same:

class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
    	    amount = amount * 1.10
        super().withdraw(amount)
        return self

class BankAccount:
    def withdraw(self, amount):
    if (self.balance - amount) > 0:
        self.balance -= amount
        else:
        print("INSUFFICIENT FUNDS")
    return self


# Overriding
# Let's talk about some other cool OOP features. Sometimes the problem with implicit inheritance is that you want the child to behave completely differently than the parent. In these cases you want to override the function, effectively replacing the functionality. To do this, just define a function with the same name in the child class. Here's an example:

class Parent:
    def method_acopy(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a() #notice this overrides the Parent method!

# in this example, we have a function named method_a() in both classes, so let's see what happens when you run it.

# invoking PARENT method_a!
# invoking CHILD method_a!
# As you can see, when we invoke dad.method_a(), it runs the Parent class' method_a() because that variable (dad) is an instance of the Parent class. However, when we invoke son.method_a(), it runs the Child class' method_a() because the variable son is an instance of the Child class. The Child overrides this method from the parent by defining its own version.

# Polymorphism
# Polymorphic behavior allows us to specify common methods in an "abstract" level and implement them in particular instances. It is the process of using an operator or function in different ways for different data input.

# We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways
class Person:
    def pay_bill(self):
        raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")

# Based on this example, a Millionaire and a Grad Student are both Persons. However, when it comes to paying a bill, how they act is quite different. This pattern is useful when you know that each subclass of a parent class must define a specific behavior in a method, and you don't want to define a default behavior in the parent class (hence the pure virtual implementation in the parent). 
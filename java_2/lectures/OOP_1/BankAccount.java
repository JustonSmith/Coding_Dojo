public class BankAccount {
    public String firstName;
    public String lastName;
    private Double accountBalance;


    // This is my constructor (similar to def __init__() method in python.)

    public BankAccount(String firstNameInput, String lastNameInput) {
        this.firstName = firstNameInput;
        this.lastName = lastNameInput;
        this.accountBalance = 0.00;
    }

    // overloading a constructor. 
    
    // This creates a bank account without needing any parameters.

    public BankAccount() {
        this.firstName = "untitled firstname";
        this.lastName = "untitled lastname";
        this.accountBalance = 0.00;
    }

    // this creates and account and also displays the initial amount. Three constructors.

    public BankAccount(String firstNameInput, String lastNameInput, Double initialAmount) {
        this.firstName = firstNameInput;
        this.lastName = lastNameInput;
        this.accountBalance = initialAmount;
    }

    // overloading a method.

    public Double deposit(Double amount) {
        this.accountBalance += amount;
        return this.accountBalance;
    }

    public Double deposit() {
        this.accountBalance += 10;
    }


// A getter to get the account balance. A getter allows you to access a variable.

    public Double getAccountBalance() {
        return this.accountBalance;
    }

    // a setter to modify the account balance. (deposit add to the balance. Setters are void and do not return anything.) Setters allow us to modify private variables.

    public void setAccountBalance(Double newBalance) {
        this.accountBalance = newBalance;
    }

    // who to send money to. (which account)
    // the amount you want to send. 
    public void transferMoney(BankAccount otherAccount, Double amountToSend) {
        // the object that called the transferMoney method is refferred to with the keyword "this".
        this.accountBalance-= amountToSend;
        otherAccount.accountBalance += amountToSend;
    }

    public String displayAccountInfo() {
        // return "Account Balance: {}, First Name: {}, Last Name: {}"
            // return "Account Balanace: " + this.accountBalance + "First Name: " + this.firstName + "Last Name" + this.lastName;

            return String.format("AccountBalance: %f, First Name: %s , Last Name: {}", this.accountBalance, this.firstName, this.lastName);
    }

}
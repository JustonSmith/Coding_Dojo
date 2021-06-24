import java.util.Random;


public class BankAccount {
    private String accountNumber = "";
    private Double checkingBalance = 0.0;
    private Double savingsBalance = 0.0;
    private static int accountsCreated = 0;
    private static Double totalMoney = 0.0;


    public void Account() {
        String accountNumber = newAccountNumber();
        Double checkingBalance = 0.0;
        Double savingsBalance = 0.0;
        accountsCreated += 1;
        System.out.println(" User account created. Account number: " + accountNumber + ".");
        System.out.println("Total number of accounts created: " + accountsCreated + ".");
    }

    public Double getChecking() {
        return checkingBalance;
    }

    public Double getSavings() {
        return savingsBalance;
    }

    public void setChecking(Double checkingBalance) {
        this.checkingBalance = checkingBalance;
    }

    public void setSavings(Double savingsBalance) {
        this.savingsBalance = savingsBalance;
    }

    private String newAccountNumber() {
        String numberTable = "0123456789";
        String randomNumber = "";

        Random random = new Random();
        
        for(int i = 0; i < 10; i++) {
            char num = numberTable.charAt(random.nextInt(100));
            randomNumber += num;
        }
        accountNumber = randomNumber;
        return randomNumber;
    }
    public void accountDeposit(String type, Double depositAmount) {
        if(type == "checking" || type == "Checking") {
            setChecking(getChecking() + depositAmount);
            totalMoney += depositAmount;
        } 
        if(type == "savings" || type == "Savings") {
            setSavings(getSavings() + depositAmount);
            totalMoney += depositAmount;

        }
        else {
            System.out.println("Please choose the correct account type.");
        }
    }

    public void accountWithdrawal(String type, Double withdrawalAmount) {
        if(type == "checking" || type == "Checking") {
            if (getChecking() < withdrawalAmount) {
                System.out.println("Insufficient Funds.");
            }
        }
            else {
            setChecking(getChecking() - withdrawalAmount);
            totalMoney -= withdrawalAmount;
            }

        }
        if(type == "savings" || type == "Savings") {
            Double withdrawalAmount;
			if(getSavings() < withdrawalAmount) {
                System.out.println("Insufficient Funds!");
            }
            else {
            setSavings(getSavings() - withdrawalAmount);
            totalMoney -= withdrawalAmount;
            }
}

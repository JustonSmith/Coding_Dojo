public class BankAccountTest {
    

    public static void main(String[] args) {
        BankAccount jeffBezosAccount = new BankAccount("Jeff", "Bezos");
        BankAccount lilWayneAccount = new BankAccount("Wayne", "Carter");
        BankAccount jColeAccount = new BankAccount("Jermaine", "Cole");
        BankAccount DiamondDarrellAccount = new BankAccount("Darrell", "Abbot");
        BankAccount untitledBankAccount = new BankAccount();
        BankAccount bobMarleyAccount = new BankAccount("Bob", "Marley", 420.00);


        System.out.println(jeffBezosAccount.getAccountBalance());
        jeffBezosAccount.deposit(1000000.00);
        Sysytem.out.println(jeffBezosAccount.getAccountBalance());
        System.out.println(jcoleAccount.getAccountBalance());
    

        jcoleAccount.deposit();
        System.out.println(jcoleAccount.getAccountBalance());
        jcoleAccount.deposit(500.00);
        System.out.println(jcoleAccount.getAccountBalance());
        jeffBezosAccount.transferMoney(LilWayneAccount, 500000.00);
        System.out.println( "J cole has this much after Jeff Bezos transferred the mula." + jcoleAccount.getAccountBalance()); // must use getter to make account balance visible.

        System.out.println(jeffBezosAccount.displayAccountInfo());

        System.out.println(untitledBankAccount.displayAccountInfo());






    }
}

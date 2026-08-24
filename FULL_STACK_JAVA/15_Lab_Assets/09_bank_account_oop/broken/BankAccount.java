// BROKEN — public balance; withdraw has no checks.

public class BankAccount {
    public String holder;
    public double balance;

    public BankAccount(String holder, double opening) {
        this.holder = holder;
        this.balance = opening;
    }

    public void withdraw(double amount) {
        balance -= amount;
    }

    public static void main(String[] args) {
        BankAccount a = new BankAccount("Anita", 100);
        a.balance = -5000;
        a.withdraw(99999);
        System.out.println(a.balance);
    }
}

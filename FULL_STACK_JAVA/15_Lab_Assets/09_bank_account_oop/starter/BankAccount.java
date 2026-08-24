// STARTER — OOP Part 1. private balance. No throw. No extends.

public class BankAccount {
    private String holder;
    private double balance;

    public BankAccount(String holder, double opening) {
        this.holder = holder;
        this.balance = opening;
    }

    public void deposit(double amount) {
        // TODO: if amount <= 0 print and return; else add to balance
    }

    public void withdraw(double amount) {
        // TODO: reject amount <= 0 and overdraft with print; else subtract
    }

    public double getBalance() {
        // TODO: return the private balance
        return 0.0;
    }

    public String getHolder() {
        return holder;
    }

    public static void main(String[] args) {
        BankAccount a = new BankAccount("Anita", 1000);
        a.deposit(200);
        a.withdraw(100);
        a.withdraw(5000);
        System.out.println(a.getHolder() + " ₹" + a.getBalance());
        // a.balance = -1;  // must not compile
    }
}

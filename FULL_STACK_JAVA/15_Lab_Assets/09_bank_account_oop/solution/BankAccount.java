// SOLUTION — BankAccount (print + return; Exceptions week adds throw).

public class BankAccount {
    private String holder;
    private double balance;

    public BankAccount(String holder, double opening) {
        this.holder = holder;
        this.balance = opening;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            System.out.println("amount must be positive");
            return;
        }
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("amount must be positive");
            return;
        }
        if (amount > balance) {
            System.out.println("insufficient funds");
            return;
        }
        balance -= amount;
    }

    public double getBalance() {
        return balance;
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
    }
}

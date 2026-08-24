// BROKEN — concrete Account; wallet pay is a typo; checkout is a type switch.

public class CampusWallet {
    public static void main(String[] args) {
        Account generic = new Account("Campus", 0);   // Bug 1: should not be constructible
        Account s = new SavingsAccount("Priya", 1000, 0.04);
        Account w = new WalletAccount("Ravi", 500);
        checkout(s, 50);
        checkout(w, 120);
        generic.printSlip();
        s.printSlip();
        w.printSlip();
    }

    static void checkout(Account a, double amount) {
        if (a.kind().equals("savings")) {            // Bug 2: type switch instead of Payable
            System.out.println("savings cannot pay here");
        } else if (a.kind().equals("wallet")) {
            ((WalletAccount) a).paay(amount);        // Bug 3: calls the typo — not Payable.pay
        } else {
            System.out.println("unknown account");
        }
    }
}

interface Payable {
    boolean pay(double amount);
}

interface Printable {
    void printSlip();
}

class Account implements Printable {                 // Bug 4: not abstract
    private String holder;
    private double balance;

    Account(String holder, double opening) {
        this.holder = holder;
        this.balance = opening;
    }

    void deposit(double amount) {
        if (amount <= 0) {
            System.out.println("amount must be positive");
            return;
        }
        balance += amount;
    }

    void withdraw(double amount) {
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

    double getBalance() {
        return balance;
    }

    String getHolder() {
        return holder;
    }

    String kind() {
        return "account";
    }

    @Override
    public void printSlip() {
        System.out.println(kind() + " | " + holder + " ₹" + (int) balance);
    }
}

class SavingsAccount extends Account {
    private double rate;

    SavingsAccount(String holder, double opening, double rate) {
        super(holder, opening);
        this.rate = rate;
    }

    @Override
    String kind() {
        return "savings";
    }

    void addInterest() {
        deposit(getBalance() * rate);
    }
}

class WalletAccount extends Account {                // Bug 5: does not implement Payable
    WalletAccount(String holder, double opening) {
        super(holder, opening);
    }

    @Override
    String kind() {
        return "wallet";
    }

    boolean paay(double amount) {                    // Bug 6: misspelled — not an override of pay
        withdraw(amount);
        return true;
    }
}

// SOLUTION — abstract Account + Payable wallet. print+return only. Account[] not ArrayList.

public class CampusWallet {
    public static void main(String[] args) {
        Account[] accounts = {
            new SavingsAccount("Priya", 1000, 0.04),
            new WalletAccount("Ravi", 500)
        };
        for (Account a : accounts) {
            a.printSlip();
        }

        Payable payable = (Payable) accounts[1];
        boolean ok = payable.pay(120);
        System.out.println("pay ok? " + ok);
        accounts[1].printSlip();

        ((SavingsAccount) accounts[0]).addInterest();
        accounts[0].printSlip();
    }
}

interface Payable {
    boolean pay(double amount);
}

interface Printable {
    void printSlip();
}

abstract class Account implements Printable {
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

    abstract String kind();

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

class WalletAccount extends Account implements Payable {
    WalletAccount(String holder, double opening) {
        super(holder, opening);
    }

    @Override
    String kind() {
        return "wallet";
    }

    @Override
    public boolean pay(double amount) {
        double before = getBalance();
        withdraw(amount);
        if (getBalance() == before) {
            return false;
        }
        System.out.println("Paid ₹" + (int) amount + " from wallet");
        return true;
    }
}

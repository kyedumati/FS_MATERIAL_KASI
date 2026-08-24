import java.util.Scanner;

// STARTER — static methods. Still one class. No throw.

public class AtmMethods {
    public static void showMenu() {
        System.out.println("1 Balance  2 Deposit  3 Withdraw  4 Quit");
    }

    public static double deposit(double balance, double amount) {
        // TODO: if amount > 0 return balance+amount; else print and return balance
        return balance;
    }

    public static double withdraw(double balance, double amount) {
        // TODO: print+return unchanged on bad/overdraft
        return balance;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double balance = 1000;
        boolean running = true;
        while (running) {
            showMenu();
            int choice = Integer.parseInt(sc.nextLine().trim());
            // TODO: call deposit/withdraw and assign balance = ...
            if (choice == 4) {
                running = false;
            }
        }
        sc.close();
    }
}

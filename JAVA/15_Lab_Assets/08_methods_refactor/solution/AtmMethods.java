import java.util.Scanner;

public class AtmMethods {
    public static void showMenu() {
        System.out.println("1 Balance  2 Deposit  3 Withdraw  4 Quit");
    }

    public static double deposit(double balance, double amount) {
        if (amount <= 0) {
            System.out.println("Enter a positive amount");
            return balance;
        }
        return balance + amount;
    }

    public static double withdraw(double balance, double amount) {
        if (amount <= 0) {
            System.out.println("Enter a positive amount");
            return balance;
        }
        if (amount > balance) {
            System.out.println("Insufficient balance");
            return balance;
        }
        System.out.println("Please take cash");
        return balance - amount;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double balance = 1000;
        boolean running = true;
        while (running) {
            showMenu();
            System.out.print("Choice: ");
            int choice = Integer.parseInt(sc.nextLine().trim());
            if (choice == 1) {
                System.out.printf("Balance: ₹%.2f%n", balance);
            } else if (choice == 2) {
                System.out.print("Amount: ");
                double amt = Double.parseDouble(sc.nextLine().trim());
                balance = deposit(balance, amt);
            } else if (choice == 3) {
                System.out.print("Amount: ");
                double amt = Double.parseDouble(sc.nextLine().trim());
                balance = withdraw(balance, amt);
            } else if (choice == 4) {
                running = false;
            } else {
                System.out.println("Unknown choice");
            }
        }
        sc.close();
        System.out.println("Thank you");
    }
}

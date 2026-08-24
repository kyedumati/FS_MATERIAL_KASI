import java.util.Scanner;

// BROKEN — does not use returned balance; withdraw always subtracts.

public class AtmMethods {
    public static void showMenu() {
        System.out.println("1 Balance  2 Deposit  3 Withdraw  4 Quit");
    }

    public static double deposit(double balance, double amount) {
        return balance + amount;
    }

    public static double withdraw(double balance, double amount) {
        return balance - amount;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double balance = 1000;
        while (true) {
            showMenu();
            int choice = Integer.parseInt(sc.nextLine().trim());
            if (choice == 2) {
                deposit(balance, Double.parseDouble(sc.nextLine().trim()));
            } else if (choice == 3) {
                withdraw(balance, Double.parseDouble(sc.nextLine().trim()));
            } else if (choice == 4) {
                break;
            }
        }
        sc.close();
    }
}

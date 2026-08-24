import java.util.Scanner;

public class AtmMenu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double balance = 1000;
        boolean running = true;
        while (running) {
            System.out.println("1 Balance  2 Deposit  3 Withdraw  4 Quit");
            System.out.print("Choice: ");
            int choice = Integer.parseInt(sc.nextLine().trim());
            if (choice == 1) {
                System.out.printf("Balance: ₹%.2f%n", balance);
            } else if (choice == 2) {
                System.out.print("Amount: ");
                double amt = Double.parseDouble(sc.nextLine().trim());
                if (amt > 0) {
                    balance = balance + amt;
                } else {
                    System.out.println("Enter a positive amount");
                }
            } else if (choice == 3) {
                System.out.print("Amount: ");
                double amt = Double.parseDouble(sc.nextLine().trim());
                if (amt <= 0) {
                    System.out.println("Enter a positive amount");
                } else if (amt > balance) {
                    System.out.println("Insufficient balance");
                } else {
                    balance = balance - amt;
                    System.out.println("Please take cash");
                }
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

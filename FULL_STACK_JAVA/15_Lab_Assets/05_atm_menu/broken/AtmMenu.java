import java.util.Scanner;

// BROKEN — infinite loop + overdraft allowed.

public class AtmMenu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double balance = 1000;
        while (true) {
            System.out.println("1 Balance  2 Deposit  3 Withdraw  4 Quit");
            int choice = Integer.parseInt(sc.nextLine().trim());
            if (choice == 1) {
                System.out.println(balance);
            } else if (choice == 2) {
                balance = balance + Double.parseDouble(sc.nextLine().trim());
            } else if (choice == 3) {
                // Bug: always subtracts, even if amount > balance
                double amt = Double.parseDouble(sc.nextLine().trim());
                balance = balance - amt;
            } else if (choice == 4) {
                // Bug: forgot break / running=false — loops forever
            }
        }
    }
}

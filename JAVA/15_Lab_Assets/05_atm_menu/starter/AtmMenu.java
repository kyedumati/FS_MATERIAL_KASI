import java.util.Scanner;

// STARTER — while/if in main only. No extra methods.

public class AtmMenu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double balance = 1000;
        boolean running = true;
        while (running) {
            System.out.println("1 Balance  2 Deposit  3 Withdraw  4 Quit");
            System.out.print("Choice: ");
            int choice = Integer.parseInt(sc.nextLine().trim());
            // TODO: handle 1-4; block overdraft; unknown choice continues
            running = false; // TODO: remove — only quit should stop
        }
        sc.close();
        System.out.println("Thank you");
    }
}

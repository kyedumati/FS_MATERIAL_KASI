import java.util.Scanner;

// BROKEN — fix 3 bugs. Linear script only.

public class CanteenCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double gstRate = 0.05;

        double price = Double.parseDouble(sc.nextLine().trim());
        int qty = Integer.parseInt(sc.nextLine().trim());
        // Bug 1: uses / instead of *
        double subtotal = price / qty;
        // Bug 2: adds gstRate as rupees, not percent
        double total = subtotal + gstRate;
        // Bug 3: should print 2 decimals with ₹
        System.out.println("Total: " + total);
        sc.close();
    }
}

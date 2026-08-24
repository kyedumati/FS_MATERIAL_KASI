import java.util.Scanner;

public class CanteenCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double gstRate = 0.05;

        System.out.print("Price: ");
        double price = Double.parseDouble(sc.nextLine().trim());
        System.out.print("Qty: ");
        int qty = Integer.parseInt(sc.nextLine().trim());

        double subtotal = price * qty;
        double total = Math.round(subtotal * (1 + gstRate) * 100.0) / 100.0;
        System.out.printf("Total: ₹%.2f%n", total);
        sc.close();
    }
}

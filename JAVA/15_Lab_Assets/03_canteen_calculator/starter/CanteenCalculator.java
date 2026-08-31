import java.util.Scanner;

// STARTER — finish TODOs. Linear script only (no if/while/for/extra methods).

public class CanteenCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double gstRate = 0.05;

        System.out.print("Price: ");
        String priceRaw = sc.nextLine().trim();
        System.out.print("Qty: ");
        String qtyRaw = sc.nextLine().trim();

        // TODO: double price = Double.parseDouble(priceRaw);
        // TODO: int qty = Integer.parseInt(qtyRaw);
        // TODO: subtotal = price * qty; total = round(subtotal * (1 + gstRate), 2)
        // TODO: System.out.printf("Total: ₹%.2f%n", total);
        System.out.println("TODO: convert, compute GST total, print");
        sc.close();
    }
}

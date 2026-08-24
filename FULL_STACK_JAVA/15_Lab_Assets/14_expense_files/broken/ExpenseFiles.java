// BROKEN — writeString truncates; no header; bare catch swallows IOException.

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public class ExpenseFiles {
    static final Path FILE = Path.of("expenses.csv");

    public static void main(String[] args) {
        appendExpense("2026-08-23", "Food", 45, "Canteen tea");
        appendExpense("2026-08-23", "Travel", 30, "Bus");
        appendExpense("2026-08-23", "Stationery", 80, "Notebook");
        listExpenses();
        System.out.println("Total INR: " + totalAmount());
    }

    static void appendExpense(String date, String category, int amountInr, String note) {
        try {
            String row = date + "," + category + "," + amountInr + "," + note + "\n";
            Files.writeString(FILE, row, StandardCharsets.UTF_8); // Bug 1: truncates — second call wipes the first
            // Bug 2: never writes a header
        } catch (Exception e) { // Bug 3: bare catch hides IOException
        }
    }

    static void listExpenses() {
        try {
            System.out.print(Files.readString(FILE, StandardCharsets.UTF_8));
        } catch (Exception e) { // Bug 4: same swallow
            System.out.println("failed");
        }
    }

    static int totalAmount() {
        try {
            String text = Files.readString(FILE, StandardCharsets.UTF_8);
            String[] lines = text.split("\n");
            int total = 0;
            for (String line : lines) {
                String[] cols = line.split(",");
                total += Integer.parseInt(cols[2]); // Bug 5: no header skip — also breaks if file was wiped to one row
            }
            return total;
        } catch (Exception e) {
            return -1; // Bug 6: magic number, same trap as Safe Input
        }
    }
}

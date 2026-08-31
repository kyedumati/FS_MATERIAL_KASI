// STARTER — File Handling. Compiles; finish header + append + list. try-with-resources + IOException.

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;

public class ExpenseFiles {
    static final Path FILE = Path.of("expenses.csv");

    public static void main(String[] args) {
        try {
            ensureHeader();
            appendExpense("2026-08-23", "Food", 45, "Canteen tea");
            appendExpense("2026-08-23", "Travel", 30, "Bus");
            appendExpense("2026-08-23", "Stationery", 80, "Notebook");
            listExpenses();
            System.out.println("Total INR: " + totalAmount());
        } catch (IOException e) {
            System.out.println("Could not use expenses.csv: " + e.getMessage());
        }
    }

    static void ensureHeader() throws IOException {
        // TODO: if Files.notExists(FILE) write header date,category,amount,note (UTF-8)
    }

    static void appendExpense(String date, String category, int amountInr, String note)
            throws IOException {
        // TODO: CREATE + APPEND one CSV row with try-with-resources BufferedWriter
        // TODO: date + "," + category + "," + amountInr + "," + note then newLine()
    }

    static void listExpenses() throws IOException {
        // TODO: read lines; skip header; print each data row
        // TODO: catch NoSuchFileException → "File not found: expenses.csv"
    }

    static int totalAmount() throws IOException {
        // TODO: sum amount column (index 2); return 0 if missing or only a header
        return 0;
    }
}

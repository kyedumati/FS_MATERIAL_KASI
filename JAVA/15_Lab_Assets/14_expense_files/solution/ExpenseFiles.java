// SOLUTION — header once, CREATE + APPEND, try-with-resources, IOException. No Git/JDBC.

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
        if (Files.notExists(FILE)) {
            Files.writeString(FILE, "date,category,amount,note\n", StandardCharsets.UTF_8);
        }
    }

    static void appendExpense(String date, String category, int amountInr, String note)
            throws IOException {
        try (BufferedWriter w = Files.newBufferedWriter(FILE, StandardCharsets.UTF_8,
                StandardOpenOption.CREATE, StandardOpenOption.APPEND)) {
            w.write(date + "," + category + "," + amountInr + "," + note);
            w.newLine();
        }
    }

    static void listExpenses() throws IOException {
        try (BufferedReader br = Files.newBufferedReader(FILE, StandardCharsets.UTF_8)) {
            String line = br.readLine(); // header
            if (line == null) {
                System.out.println("no rows");
                return;
            }
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (NoSuchFileException e) {
            System.out.println("File not found: " + FILE.getFileName());
        }
    }

    static int totalAmount() throws IOException {
        if (Files.notExists(FILE)) {
            return 0;
        }
        int total = 0;
        try (BufferedReader br = Files.newBufferedReader(FILE, StandardCharsets.UTF_8)) {
            String line = br.readLine(); // header
            while ((line = br.readLine()) != null) {
                String[] cols = line.split(",");
                if (cols.length >= 3) {
                    total += Integer.parseInt(cols[2]);
                }
            }
        }
        return total;
    }
}

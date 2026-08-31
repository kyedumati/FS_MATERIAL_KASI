// BROKEN — hard-coded password; Statement + concat SQL; leaked Connection; bare catch.

import java.math.BigDecimal;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class LibraryCrud {
    public static void main(String[] args) {
        listByAuthor("Chetan Bhagat");
        addBook("CampusCart Cookbook", "Priya Rao", 1, new BigDecimal("249.00"));
    }

    static void listByAuthor(String author) {
        try {
            // Bug 1: password in source (never do this — use .env / getenv)
            Connection conn = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/training_db", "root", "root123");
            Statement stmt = conn.createStatement();
            // Bug 2: string-concat SQL — author can change the command (SQL injection)
            String sql = "SELECT title, author FROM books WHERE author = '" + author + "'";
            ResultSet rs = stmt.executeQuery(sql);
            while (rs.next()) {
                System.out.println(rs.getString("title") + " — " + rs.getString("author"));
            }
            // Bug 3: never close conn / stmt / rs (no try-with-resources)
        } catch (Exception e) { // Bug 4: bare catch hides SQLException
        }
    }

    static void addBook(String title, String author, int copies, BigDecimal priceInr) {
        try {
            Connection conn = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/training_db", "root", "root123");
            Statement stmt = conn.createStatement();
            // Bug 5: INSERT built with quotes in Java — same injection hole
            String sql = "INSERT INTO books (title, author, copies, price_inr) VALUES ('"
                    + title + "', '" + author + "', " + copies + ", " + priceInr + ")";
            stmt.execute(sql);
            System.out.println("inserted?");
        } catch (Exception e) {
        }
    }
}

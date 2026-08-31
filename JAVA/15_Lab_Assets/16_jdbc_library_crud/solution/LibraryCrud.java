// SOLUTION — try-with-resources Connection; PreparedStatement ? only; password from env / .env.
// No Spring / JPA / Lombok / DataSource. Connector/J on java -cp.

import java.io.IOException;
import java.math.BigDecimal;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class LibraryCrud {
    public static void main(String[] args) {
        try (Connection conn = openConnection()) {
            System.out.println("Connected to " + conn.getCatalog());
            listBooks(conn);
            addBook(conn, "CampusCart Cookbook", "Priya Rao", 1, new BigDecimal("249.00"));
            updateCopies(conn, "CampusCart Cookbook", 3);
            System.out.println("--- after insert + update ---");
            listBooks(conn);
            deleteByTitle(conn, "CampusCart Cookbook");
            System.out.println("--- after delete ---");
            listBooks(conn);
        } catch (SQLException e) {
            System.out.println("Could not talk to MySQL: " + e.getMessage());
        }
    }

    static Connection openConnection() throws SQLException {
        String host = getenvOrDotEnv("MYSQL_HOST");
        if (host == null) {
            host = "localhost";
        }
        String port = getenvOrDotEnv("MYSQL_PORT");
        if (port == null) {
            port = "3306";
        }
        String user = getenvOrDotEnv("MYSQL_USER");
        if (user == null) {
            user = "root";
        }
        String database = getenvOrDotEnv("MYSQL_DATABASE");
        if (database == null) {
            database = "training_db";
        }
        String password = getenvOrDotEnv("MYSQL_PASSWORD");
        if (password == null || password.length() == 0 || password.equals("change_me")) {
            throw new SQLException("Set MYSQL_PASSWORD in the environment or in .env (copy .env.example)");
        }
        String url = jdbcUrl(host, port, database);
        return DriverManager.getConnection(url, user, password);
    }

    static void listBooks(Connection conn) throws SQLException {
        String sql = "SELECT title, author, copies, price_inr FROM books ORDER BY book_id";
        try (PreparedStatement ps = conn.prepareStatement(sql);
                ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                System.out.println(rs.getString("title") + " | " + rs.getString("author")
                        + " | copies=" + rs.getInt("copies") + " | ₹" + rs.getBigDecimal("price_inr"));
            }
        }
    }

    static void addBook(Connection conn, String title, String author, int copies, BigDecimal priceInr)
            throws SQLException {
        String sql = "INSERT INTO books (title, author, copies, price_inr) VALUES (?, ?, ?, ?)";
        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, title);
            ps.setString(2, author);
            ps.setInt(3, copies);
            ps.setBigDecimal(4, priceInr);
            int n = ps.executeUpdate();
            System.out.println("Inserted rows: " + n);
        }
    }

    static void updateCopies(Connection conn, String title, int copies) throws SQLException {
        String sql = "UPDATE books SET copies = ? WHERE title = ?";
        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, copies);
            ps.setString(2, title);
            System.out.println("Updated rows: " + ps.executeUpdate());
        }
    }

    static void deleteByTitle(Connection conn, String title) throws SQLException {
        String sql = "DELETE FROM books WHERE title = ?";
        try (PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, title);
            System.out.println("Deleted rows: " + ps.executeUpdate());
        }
    }

    static String getenvOrDotEnv(String key) {
        String fromEnv = System.getenv(key);
        if (fromEnv != null && fromEnv.length() > 0) {
            return fromEnv;
        }
        Path envFile = Path.of(".env");
        if (Files.notExists(envFile)) {
            return null;
        }
        try {
            for (String line : Files.readAllLines(envFile, StandardCharsets.UTF_8)) {
                line = line.trim();
                if (line.length() == 0 || line.startsWith("#") || !line.contains("=")) {
                    continue;
                }
                int eq = line.indexOf('=');
                String k = line.substring(0, eq).trim();
                String v = line.substring(eq + 1).trim();
                if (k.equals(key)) {
                    return v;
                }
            }
        } catch (IOException e) {
            System.out.println("Could not read .env: " + e.getMessage());
        }
        return null;
    }

    static String jdbcUrl(String host, String port, String database) {
        return "jdbc:mysql://" + host + ":" + port + "/" + database
                + "?allowPublicKeyRetrieval=true&useSSL=false&serverTimezone=Asia/Kolkata";
    }
}

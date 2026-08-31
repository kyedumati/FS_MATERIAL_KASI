// STARTER — JDBC library CRUD. Compiles; finish connect + PreparedStatement ?.
// Copy ../.env.example to .env. Connector/J must be on java -cp. No Spring.

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
            listBooks(conn);
            deleteByTitle(conn, "CampusCart Cookbook");
            System.out.println("After delete:");
            listBooks(conn);
        } catch (SQLException e) {
            System.out.println("Could not talk to MySQL: " + e.getMessage());
        }
    }

    static Connection openConnection() throws SQLException {
        // TODO: host/user/db from getenvOrDotEnv; DriverManager.getConnection
        // TODO: URL like jdbc:mysql://host:port/db?allowPublicKeyRetrieval=true&useSSL=false&serverTimezone=Asia/Kolkata
        throw new SQLException("TODO: openConnection");
    }

    static void listBooks(Connection conn) throws SQLException {
        // TODO: PreparedStatement SELECT title, author, copies, price_inr ORDER BY book_id
        // TODO: set no parameters; executeQuery; print each row
    }

    static void addBook(Connection conn, String title, String author, int copies, BigDecimal priceInr)
            throws SQLException {
        // TODO: INSERT INTO books (title, author, copies, price_inr) VALUES (?, ?, ?, ?)
        // TODO: setString / setInt / setBigDecimal; executeUpdate; print row count
    }

    static void updateCopies(Connection conn, String title, int copies) throws SQLException {
        // TODO: UPDATE books SET copies = ? WHERE title = ?
        // TODO: executeUpdate; print rows updated
    }

    static void deleteByTitle(Connection conn, String title) throws SQLException {
        // TODO: DELETE FROM books WHERE title = ?
        // TODO: executeUpdate; print rows deleted
    }

    /** Env first, then a local .env file (Git week: never commit .env). */
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

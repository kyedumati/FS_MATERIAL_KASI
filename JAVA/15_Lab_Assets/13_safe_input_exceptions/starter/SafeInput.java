// STARTER — Exceptions. Compiles; finish readAge. No files.

public class SafeInput {
    public static void main(String[] args) {
        String[] samples = {"21", "abc", "0", "200"};
        for (String sample : samples) {
            try {
                System.out.println(sample + " -> " + readAge(sample));
            } catch (NumberFormatException e) {
                System.out.println(sample + " NumberFormatException " + e.getMessage());
            } catch (InvalidAgeException e) {
                System.out.println(sample + " InvalidAgeException " + e.getMessage());
            }
        }
    }

    static int readAge(String raw) throws InvalidAgeException {
        // TODO: Integer.parseInt(raw.trim())
        // TODO: if age < 1 or age > 120 throw new InvalidAgeException("age out of range: " + age)
        // TODO: on NumberFormatException throw new NumberFormatException("age must be an integer")
        return 0;
    }
}

class InvalidAgeException extends Exception {
    InvalidAgeException(String message) {
        super(message);
    }
}

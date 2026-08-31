// SOLUTION — NumberFormatException vs InvalidAgeException. No files.

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
        int age;
        try {
            age = Integer.parseInt(raw.trim());
        } catch (NumberFormatException e) {
            throw new NumberFormatException("age must be an integer");
        }
        if (age < 1 || age > 120) {
            throw new InvalidAgeException("age out of range: " + age);
        }
        return age;
    }
}

class InvalidAgeException extends Exception {
    InvalidAgeException(String message) {
        super(message);
    }
}

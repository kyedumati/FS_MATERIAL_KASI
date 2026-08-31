// BROKEN — off-by-one mask + no trim.

public class FieldCleaner {
    public static void main(String[] args) {
        String email = "  Ravi@Gmail.COM ";
        System.out.println(email.toLowerCase()); // Bug: no trim

        String phone = "9876543210";
        // Bug: substring too short / wrong start
        String mask = "****" + phone.substring(8);
        System.out.println(mask);
    }
}

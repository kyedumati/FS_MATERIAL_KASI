import java.util.Scanner;

// STARTER — string methods + for. No extra methods.

public class FieldCleaner {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Email: ");
        String emailRaw = sc.nextLine();
        System.out.print("Phone: ");
        String phoneRaw = sc.nextLine();

        // TODO: email = trim + toLowerCase
        // TODO: digits only from phone; print whether length == 10
        // TODO: mask ****** + last 4 digits
        System.out.println("TODO");
        sc.close();
    }
}

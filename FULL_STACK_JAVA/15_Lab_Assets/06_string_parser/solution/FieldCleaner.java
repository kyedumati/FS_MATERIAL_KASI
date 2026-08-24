import java.util.Scanner;

public class FieldCleaner {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Email: ");
        String email = sc.nextLine().trim().toLowerCase();
        System.out.print("Phone: ");
        String phoneRaw = sc.nextLine();

        String digits = "";
        for (int i = 0; i < phoneRaw.length(); i++) {
            char c = phoneRaw.charAt(i);
            if (c >= '0' && c <= '9') {
                digits = digits + c;
            }
        }

        System.out.println(email);
        System.out.println("Ten digits: " + (digits.length() == 10));
        if (digits.length() >= 4) {
            System.out.println("******" + digits.substring(digits.length() - 4));
        } else {
            System.out.println("Phone too short to mask");
        }
        sc.close();
    }
}

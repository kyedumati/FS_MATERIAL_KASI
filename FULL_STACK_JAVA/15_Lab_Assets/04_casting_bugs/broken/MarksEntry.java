import java.util.Scanner;

// BROKEN — casting bugs.

public class MarksEntry {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Bug 1: parseInt rejects 78.5
        System.out.print("Subject 1: ");
        int m1 = Integer.parseInt(sc.nextLine().trim());
        System.out.print("Subject 2: ");
        int m2 = Integer.parseInt(sc.nextLine().trim());
        System.out.print("Subject 3: ");
        int m3 = Integer.parseInt(sc.nextLine().trim());

        double avg = (m1 + m2 + m3) / 3.0;
        // Bug 2+3: truncates display
        System.out.println("Average: " + (int) avg);
        sc.close();
    }
}

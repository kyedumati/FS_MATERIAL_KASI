import java.util.Scanner;

public class MarksEntry {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Subject 1: ");
        double m1 = Double.parseDouble(sc.nextLine().trim());
        System.out.print("Subject 2: ");
        double m2 = Double.parseDouble(sc.nextLine().trim());
        System.out.print("Subject 3: ");
        double m3 = Double.parseDouble(sc.nextLine().trim());
        double avg = (m1 + m2 + m3) / 3.0;
        System.out.printf("Average: %.2f%n", avg);
        sc.close();
    }
}

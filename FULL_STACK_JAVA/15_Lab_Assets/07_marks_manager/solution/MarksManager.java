import java.util.Scanner;

public class MarksManager {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] marks = new int[20];
        int count = 0;
        boolean running = true;
        while (running) {
            System.out.println("1 Add  2 List  3 Average  4 Toppers  5 Quit");
            System.out.print("Choice: ");
            int choice = Integer.parseInt(sc.nextLine().trim());
            if (choice == 1) {
                if (count >= marks.length) {
                    System.out.println("Full");
                } else {
                    System.out.print("Mark 0-100: ");
                    int m = Integer.parseInt(sc.nextLine().trim());
                    if (m < 0 || m > 100) {
                        System.out.println("Out of range");
                    } else {
                        marks[count] = m;
                        count++;
                    }
                }
            } else if (choice == 2) {
                if (count == 0) {
                    System.out.println("No marks yet");
                } else {
                    for (int i = 0; i < count; i++) {
                        System.out.println(marks[i]);
                    }
                }
            } else if (choice == 3) {
                if (count == 0) {
                    System.out.println("No marks yet");
                } else {
                    int sum = 0;
                    for (int i = 0; i < count; i++) {
                        sum += marks[i];
                    }
                    System.out.printf("Average: %.2f%n", sum / (double) count);
                }
            } else if (choice == 4) {
                int n = 0;
                for (int i = 0; i < count; i++) {
                    if (marks[i] >= 90) {
                        System.out.println(marks[i]);
                        n++;
                    }
                }
                if (n == 0) {
                    System.out.println("No toppers");
                }
            } else if (choice == 5) {
                running = false;
            } else {
                System.out.println("Unknown choice");
            }
        }
        sc.close();
    }
}

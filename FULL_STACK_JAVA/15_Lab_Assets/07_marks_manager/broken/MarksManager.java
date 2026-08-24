import java.util.Scanner;

// BROKEN — divide by zero; loops full array not count.

public class MarksManager {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] marks = new int[20];
        int count = 0;
        while (true) {
            System.out.println("1 Add  2 List  3 Average  4 Quit");
            int choice = Integer.parseInt(sc.nextLine().trim());
            if (choice == 1) {
                marks[count] = Integer.parseInt(sc.nextLine().trim());
                count++;
            } else if (choice == 2) {
                for (int i = 0; i < marks.length; i++) {
                    System.out.println(marks[i]);
                }
            } else if (choice == 3) {
                int sum = 0;
                for (int i = 0; i < count; i++) {
                    sum += marks[i];
                }
                System.out.println(sum / count);
            } else if (choice == 4) {
                break;
            }
        }
        sc.close();
    }
}

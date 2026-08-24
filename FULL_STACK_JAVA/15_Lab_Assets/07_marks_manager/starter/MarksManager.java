import java.util.Scanner;

// STARTER — array + count + while menu. No extra methods. No ArrayList.

public class MarksManager {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] marks = new int[20];
        int count = 0;
        boolean running = true;
        while (running) {
            System.out.println("1 Add  2 List  3 Average  4 Toppers  5 Quit");
            int choice = Integer.parseInt(sc.nextLine().trim());
            // TODO: add 0-100 if count < 20; list 0..count-1; avg if count>0; toppers >=90
            running = false;
        }
        sc.close();
    }
}

import java.util.Scanner;

// STARTER — three marks average (double + printf; no if/extra methods yet).

public class MarksEntry {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Subject 1: ");
        String m1 = sc.nextLine();
        System.out.print("Subject 2: ");
        String m2 = sc.nextLine();
        System.out.print("Subject 3: ");
        String m3 = sc.nextLine();
        // TODO: Double.parseDouble each; avg = (a+b+c)/3.0; printf Average: xx.xx
        System.out.println("TODO: convert with parseDouble, print average");
        sc.close();
    }
}

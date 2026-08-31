// BROKEN — bare catch swallows errors; no range; no custom exception.

public class SafeInput {
    public static void main(String[] args) {
        String[] samples = {"21", "abc", "0", "200"};
        for (String sample : samples) {
            System.out.println(sample + " -> " + readAge(sample));
        }
    }

    static int readAge(String raw) {
        try {
            return Integer.parseInt(raw); // Bug 1: no trim; Bug 2: no range
        } catch (Exception e) {           // Bug 3: bare-broad catch hides the type
            return -1;                    // Bug 4: swallows — caller thinks -1 is an age
        }
    }
}


import java.util.Scanner;

public class patturn_for {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter N: ");
        int N = sc.nextInt();

        System.out.println("\n========== PATTERN 1: FULL SQUARE ==========");
        // Print N x N square of stars
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 2: RIGHT TRIANGLE (ASCENDING) ==========");
        // Print right triangle with increasing stars
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 3: RIGHT TRIANGLE (DESCENDING) ==========");
        // Print right triangle with decreasing stars
        for (int i = N; i >= 1; i--) {
            for (int j = 1; j <= i; j++) { 
                System.out.print("* ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 4: LEFT TRIANGLE (NUMBERS) ==========");
        // Print triangle with numbers 
        for (int i = 1; i <= N; i++) { // N = 5, Outer loop for rows : i = 1 to N , i++ (incrementing) print i stars in each row
            for (int j = 1; j <= i; j++) { // Inner loop for columns : j = 1 to i , j++ (incrementing) print j in each column
                System.out.print(j + " ");// Print j in each column
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 5: PYRAMID (CENTERED) ==========");
        // Print centered pyramid
        for (int i = 1; i <= N; i++) {// N = 5, Outer loop for rows : i = 1 to N , i++ (incrementing) print i stars in each row
            for (int j = 1; j <= N - i; j++) {// Inner loop for spaces : j = 1 to N - i , j++ (incrementing) print space in each column
                System.out.print(" ");// Print space in each column
            }
            for (int j = 1; j <= i; j++) {// Inner loop for stars : j = 1 to i , j++ (incrementing) print * in each column
                System.out.print("* ");// Print * in each column
            }
            System.out.println();// Move to the next line after each row is printed     
        }

        System.out.println("\n========== PATTERN 6: INVERTED PYRAMID ==========");
        // Print inverted pyramid
        for (int i = N; i >= 1; i--) {
            for (int j = 1; j <= N - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 7: DIAMOND ==========");
        // Print diamond pattern (top half)
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        // Print diamond pattern (bottom half)
        for (int i = N - 1; i >= 1; i--) {
            for (int j = 1; j <= N - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 8: HOLLOW SQUARE ==========");
        // Print hollow square
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (i == 1 || i == N || j == 1 || j == N) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 9: FLOYD'S TRIANGLE ==========");
        // Print Floyd's triangle with numbers
        int count = 1;
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(count + " ");
                count++;
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 10: PASCAL'S TRIANGLE ==========");
        // Print Pascal's triangle
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N - i; j++) {
                System.out.print(" ");
            }
            int num = 1;
            for (int j = 0; j <= i; j++) {
                System.out.print(num + " ");
                num = num * (i - j) / (j + 1);
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 11: NUMBER PYRAMID ==========");
        // Print pyramid with each row containing row number
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print(i + " ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 12: HOURGLASS ==========");
        // Print hourglass (top half descending)
        for (int i = N; i >= 1; i--) {
            for (int j = 1; j <= N - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        // Print hourglass (bottom half ascending)
        for (int i = 2; i <= N; i++) {
            for (int j = 1; j <= N - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 13: X PATTERN ==========");
        // Print X pattern
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (i == j || i + j == N + 1) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 14: Z PATTERN ==========");
        // Print Z pattern
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (i == 1 || i == N || i + j == N + 1) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 15: BUTTERFLY PATTERN ==========");
        // Print butterfly (left side top)
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            for (int j = 1; j <= 2 * (N - i); j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        // Print butterfly (left side bottom)
        for (int i = N; i >= 1; i--) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            for (int j = 1; j <= 2 * (N - i); j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 16: ALPHABETIC TRIANGLE ==========");
        // Print triangle with alphabets
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print((char) (64 + j) + " ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 17: RIGHT ANGLE TRIANGLE ==========");
        // Print right angle triangle (rotated)
        for (int i = 1; i <= N; i++) {
            for (int j = N - i; j > 0; j--) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 18: HALF PYRAMID ==========");
        // Print half pyramid
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 19: STAIRCASE PATTERN ==========");
        // Print staircase
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j < i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= N - i + 1; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 20: ARROW PATTERN ==========");
        // Print arrow (top half)
        for (int i = 1; i <= N; i++) {
            for (int j = N - i; j > 0; j--) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        // Print arrow (bottom half)
        for (int i = N - 1; i >= 1; i--) {
            for (int j = N - i; j > 0; j--) {
                System.out.print(" ");
            }
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 21: CROSS PATTERN ==========");
        // Print cross (+ pattern)
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (i == N / 2 + 1 || j == N / 2 + 1) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 22: SQUARE SPIRAL ==========");
        // Print decreasing sequence in rows
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N - i + 1; j++) {
                System.out.print((j) + " ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 23: HOLLOW DIAMOND ==========");
        // Print hollow diamond (top half)
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N - i; j++) {
                System.out.print(" ");
            }
            System.out.print("*");
            if (i > 1) {
                for (int j = 1; j <= 2 * i - 3; j++) {
                    System.out.print(" ");
                }
                System.out.print("*");
            }
            System.out.println();
        }
        // Print hollow diamond (bottom half)
        for (int i = N - 1; i >= 1; i--) {
            for (int j = 1; j <= N - i; j++) {
                System.out.print(" ");
            }
            System.out.print("*");
            if (i > 1) {
                for (int j = 1; j <= 2 * i - 3; j++) {
                    System.out.print(" ");
                }
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 24: REVERSE NUMBER TRIANGLE ==========");
        // Print reverse number triangle
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print((i - j + 1) + " ");
            }
            System.out.println();
        }

        System.out.println("\n========== PATTERN 25: ZIGZAG PATTERN ==========");
        // Print zigzag pattern
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if ((i + j) % 2 == 0) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
            }
            System.out.println();
        }

        sc.close();
    }
}

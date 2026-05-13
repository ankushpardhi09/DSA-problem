import java.util.Scanner;

class patturn_while {

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter N: ");
            int N = sc.nextInt();

        System.out.println("\n========== PATTERN 1: FULL SQUARE ==========");
        // Print N x N square of stars
        int i = 0;
        while (i < N) {
            int j = 0;
            while (j < N) {
                System.out.print("* ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 2: RIGHT TRIANGLE (ASCENDING) ==========");
        // Print right triangle with increasing stars
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= i) {
                System.out.print("* ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 3: RIGHT TRIANGLE (DESCENDING) ==========");
        // Print right triangle with decreasing stars
        i = N;
        while (i >= 1) {
            int j = 1;
            while (j <= i) {
                System.out.print("* ");
                j++;
            }
            System.out.println();
            i--;
        }

        System.out.println("\n========== PATTERN 4: LEFT TRIANGLE (NUMBERS) ==========");
        // Print triangle with numbers
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= i) {
                System.out.print(j + " ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 5: PYRAMID (CENTERED) ==========");
        // Print centered pyramid
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= N - i) {
                System.out.print(" ");
                j++;
            }
            j = 1;
            while (j <= i) {
                System.out.print("* ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 6: INVERTED PYRAMID ==========");
        // Print inverted pyramid
        i = N;
        while (i >= 1) {
            int j = 1;
            while (j <= N - i) {
                System.out.print(" ");
                j++;
            }
            j = 1;
            while (j <= i) {
                System.out.print("* ");
                j++;
            }
            System.out.println();
            i--;
        }

        System.out.println("\n========== PATTERN 7: DIAMOND ==========");
        // Print diamond pattern (top half)
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= N - i) {
                System.out.print(" ");
                j++;
            }
            j = 1;
            while (j <= 2 * i - 1) {
                System.out.print("*");
                j++;
            }
            System.out.println();
            i++;
        }
        // Print diamond pattern (bottom half)
        i = N - 1;
        while (i >= 1) {
            int j = 1;
            while (j <= N - i) {
                System.out.print(" ");
                j++;
            }
            j = 1;
            while (j <= 2 * i - 1) {
                System.out.print("*");
                j++;
            }
            System.out.println();
            i--;
        }

        System.out.println("\n========== PATTERN 8: HOLLOW SQUARE ==========");
        // Print hollow square
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= N) {
                if (i == 1 || i == N || j == 1 || j == N) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 9: FLOYD'S TRIANGLE ==========");
        // Print Floyd's triangle with numbers
        int count = 1;
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= i) {
                System.out.print(count + " ");
                count++;
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 10: PASCAL'S TRIANGLE ==========");
        // Print Pascal's triangle
        i = 0;
        while (i < N) {
            int j = 0;
            while (j < N - i) {
                System.out.print(" ");
                j++;
            }
            int num = 1;
            j = 0;
            while (j <= i) {
                System.out.print(num + " ");
                num = num * (i - j) / (j + 1);
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 11: NUMBER PYRAMID ==========");
        // Print pyramid with each row containing row number
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= N - i) {
                System.out.print(" ");
                j++;
            }
            j = 1;
            while (j <= i) {
                System.out.print(i + " ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 12: HOURGLASS ==========");
        // Print hourglass (top half descending)
        i = N;
        while (i >= 1) {
            int j = 1;
            while (j <= N - i) {
                System.out.print(" ");
                j++;
            }
            j = 1;
            while (j <= i) {
                System.out.print("* ");
                j++;
            }
            System.out.println();
            i--;
        }
        // Print hourglass (bottom half ascending)
        i = 2;
        while (i <= N) {
            int j = 1;
            while (j <= N - i) {
                System.out.print(" ");
                j++;
            }
            j = 1;
            while (j <= i) {
                System.out.print("* ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 13: X PATTERN ==========");
        // Print X pattern
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= N) {
                if (i == j || i + j == N + 1) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 14: Z PATTERN ==========");
        // Print Z pattern
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= N) {
                if (i == 1 || i == N || i + j == N + 1) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 15: BUTTERFLY PATTERN ==========");
        // Print butterfly (left side top)
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= i) {
                System.out.print("*");
                j++;
            }
            j = 1;
            while (j <= 2 * (N - i)) {
                System.out.print(" ");
                j++;
            }
            j = 1;
            while (j <= i) {
                System.out.print("*");
                j++;
            }
            System.out.println();
            i++;
        }
        // Print butterfly (left side bottom)
        i = N;
        while (i >= 1) {
            int j = 1;
            while (j <= i) {
                System.out.print("*");
                j++;
            }
            j = 1;
            while (j <= 2 * (N - i)) {
                System.out.print(" ");
                j++;
            }
            j = 1;
            while (j <= i) {
                System.out.print("*");
                j++;
            }
            System.out.println();
            i--;
        }

        System.out.println("\n========== PATTERN 16: ALPHABETIC TRIANGLE ==========");
        // Print triangle with alphabets
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= i) {
                System.out.print((char) (64 + j) + " ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 17: RIGHT ANGLE TRIANGLE ==========");
        // Print right angle triangle (rotated)
        i = 1;
        while (i <= N) {
            int j = N - i;
            while (j > 0) {
                System.out.print(" ");
                j--;
            }
            j = 1;
            while (j <= i) {
                System.out.print("* ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 18: HALF PYRAMID ==========");
        // Print half pyramid
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= i) {
                System.out.print("* ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 19: STAIRCASE PATTERN ==========");
        // Print staircase
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j < i) {
                System.out.print(" ");
                j++;
            }
            j = 1;
            while (j <= N - i + 1) {
                System.out.print("* ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 20: ARROW PATTERN ==========");
        // Print arrow (top half)
        i = 1;
        while (i <= N) {
            int j = N - i;
            while (j > 0) {
                System.out.print(" ");
                j--;
            }
            j = 1;
            while (j <= i) {
                System.out.print("*");
                j++;
            }
            System.out.println();
            i++;
        }
        // Print arrow (bottom half)
        i = N - 1;
        while (i >= 1) {
            int j = N - i;
            while (j > 0) {
                System.out.print(" ");
                j--;
            }
            j = 1;
            while (j <= i) {
                System.out.print("*");
                j++;
            }
            System.out.println();
            i--;
        }

        System.out.println("\n========== PATTERN 21: CROSS PATTERN ==========");
        // Print cross (+ pattern)
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= N) {
                if (i == N / 2 + 1 || j == N / 2 + 1) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 22: SQUARE SPIRAL ==========");
        // Print decreasing sequence in rows
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= N - i + 1) {
                System.out.print((j) + " ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 23: HOLLOW DIAMOND ==========");
        // Print hollow diamond (top half)
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= N - i) {
                System.out.print(" ");
                j++;
            }
            System.out.print("*");
            if (i > 1) {
                j = 1;
                while (j <= 2 * i - 3) {
                    System.out.print(" ");
                    j++;
                }
                System.out.print("*");
            }
            System.out.println();
            i++;
        }
        // Print hollow diamond (bottom half)
        i = N - 1;
        while (i >= 1) {
            int j = 1;
            while (j <= N - i) {
                System.out.print(" ");
                j++;
            }
            System.out.print("*");
            if (i > 1) {
                j = 1;
                while (j <= 2 * i - 3) {
                    System.out.print(" ");
                    j++;
                }
                System.out.print("*");
            }
            System.out.println();
            i--;
        }

        System.out.println("\n========== PATTERN 24: REVERSE NUMBER TRIANGLE ==========");
        // Print reverse number triangle
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= i) {
                System.out.print((i - j + 1) + " ");
                j++;
            }
            System.out.println();
            i++;
        }

        System.out.println("\n========== PATTERN 25: ZIGZAG PATTERN ==========");
        // Print zigzag pattern
        i = 1;
        while (i <= N) {
            int j = 1;
            while (j <= N) {
                if ((i + j) % 2 == 0) {
                    System.out.print("* ");
                } else {
                    System.out.print("  ");
                }
                j++;
            }
            System.out.println();
            i++;
        }
        } // End of try-with-resources
    }
}

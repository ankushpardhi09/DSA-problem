class Solution {
    // Function to check if a given integer is a palindrome
    public boolean palindrome(int n) {
        int revNum = 0; // Initialize a variable to store the reverse of the number
        int dup = n; // Create a duplicate variable to store the original number

        // Iterate through each digit of the number until it becomes 0
        while (n > 0) {
            int ld = n % 10; // Extract the last digit of the number
            revNum = (revNum * 10) + ld; // Build the reverse number by appending the last digit
            n = n / 10; // Remove the last digit from the original number
        }

        // Check if the original number is equal to its reverse
        return dup == revNum; // Return true if they are equal, otherwise false
    }
}

public class problems {
    public static void main(String[] args) {
        int number = 4554; // Example number
        Solution obj = new Solution();
        if (obj.palindrome(number)) { // Check if the number is a palindrome
            System.out.println(number + " is a palindrome.");
        } else {
            System.out.println(number + " is not a palindrome.");
        }
    }
}

// input: 4554
// output: 4554 is a palindrome.

/*while (n > 0) {
            int ld = n % 10;  4 is the last digit of 4554 , 5 is the last digit of 455 , 5 is the last digit of 45 , 4 is the last digit of 4
            revNum = (revNum * 10) + ld; revNum = (0 * 10) + 4 = 4 , revNum = (4 * 10) + 5 = 45 , revNum = (45 * 10) + 5 = 455 , revNum = (455 * 10) + 4 = 4554
            n = n / 10; n = 4554 / 10 = 455, n = 455 / 10 = 45 , n = 45 / 10 = 4 , n = 4 / 10 = 0
        }
        return dup == revNum; dup = 4554 , revNum = 4554 , 4554 == 4554 is true
    }  }   */
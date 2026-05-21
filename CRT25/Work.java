import java.util.Scanner;
public class Work {

    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    //System.out.print("Enter a number: ");
// Write a Java program to culculate the square and cube of a number entered by the user.
    // int num = sc.nextInt();
    // int square = num * num;
    // int cube = num * num * num;
    // System.out.println("Square of " + num + " is: " + square);
    // System.out.println("Cube of " + num + " is: " + cube);

// 2. Write a Java program to check whther n given integer is positive, negative or Zero.
//    if(num > 0){
//     System.out.println("number is Positive" + num);
//    } else if (num < 0){
//     System.out.println("number is Negtive" + num);
//     }else{
//         System.out.println("number is Zero" + num);
//     }
   
// 3. Write i ava prournm to calculate Simple Interest.
    // System.out.println("Enter Principle Amount:");
    // double principle = sc.nextDouble();
    // System.out.println("Enter rate of Inmterest: ");
    // int rate = sc.nextInt();
    // System.out.println("Enter time in years: ");
    // Double time = sc.nextDouble();
    // double simpleInterest = (principle * rate * time) / 100; 
    // System.out.println("Simple Interest is: " + simpleInterest);   

// 4. Write a Java program to count the total number of digits in a given integer.
    //  System.out.println("Enter a Number for Counter");
    //  int Count = sc.nextInt();
    //  int TotalDight = 0;
    //     while(Count != 0){
    //         Count = Count / 10;
    //         TotalDight++;
    //  }
    //     System.out.println("Total Dight is: " + TotalDight);

// 5. Write a Java program to reverse a given integer number without converting it into a string.
        System.out.println("Enter a Number to Reverse");
        int Reverse = sc.nextInt();
        int ReversedNumber = 0;
            while(Reverse != 0){
                int digit = Reverse % 10;
                ReversedNumber = ReversedNumber * 10 + digit;
                Reverse = Reverse / 10;
        }
            System.out.println("Reversed Number is: " + ReversedNumber);
            
// 6. Write a Java program to accept a character from the user and determine whether it is uppercase,
// lowercase, a digit, or a special symbol.
// 7. Write a Java program to check whether a given year is a leap-year or not.

    }
}

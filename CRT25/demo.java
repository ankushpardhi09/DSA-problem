
public class demo {

    public static void main(String[] args) {

        int arr[][] = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        for (int i = 0; i < 3; i++) {// row
            int sum = 0;
            for (int j = 0; j < 3; j++) { // column
                sum += arr[i][j];
            }
            System.out.println("Sum of row " + (i+1) + ": " + sum);
        }

        for (int j = 0; j < 3; j++) { // column
            int sum = 0;
            for (int i = 0; i < 3; i++) { // row
                sum += arr[i][j];
            }
            System.out.println("Sum of column " + (j+1) + ": " + sum);
        }

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (arr[i][j] < min) min = arr[i][j];
                if (arr[i][j] > max) max = arr[i][j];
            }
        }
        System.out.println("Minimum number: " + min);
        System.out.println("Maximum number: " + max);
    }
}

//     System.out.print("Enter size of array:");
//   Scanner sc = new Scanner(System.in);
//   int size = sc.nextInt();
//   int[] a = new int[size];
//     for(int i=0;i<size;i++){
//     System.out.println("Enter element at index "+i+":");
//         a[i]=sc.nextInt();
//     }
// int arr[] = new int[10];
// System.out.println("Enter 10 elements:");
// for(int i=0;i<10;i++){
//     arr[i]=sc.nextInt();
        //     System.err.println("Element at index "+i+" is: "+arr[i]);   

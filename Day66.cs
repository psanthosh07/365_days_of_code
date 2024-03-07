using System;

class Program {
    public static void Main(string[] args) {
        // Read the number of elements in the array
        int N = int.Parse(Console.ReadLine());

        // Create an array to store the elements
        int[] arr = new int[N];

        // Read the array elements
        for (int i = 0; i < N; i++) {
            arr[i] = int.Parse(Console.ReadLine());
        }

        // Print the array in reverse order
        for (int i = N - 1; i >= 0; i--) {
            Console.WriteLine(arr[i]);
        }
    }
}

using System;

class MAIN {
    public static void Main(string[] args) {
        int num1 = Convert.ToInt32(Console.ReadLine());

        int factorial = 1;
        for (int i = 1; i <= num1; i++) {
            factorial *= i;
        }
        Console.WriteLine(factorial);

        int num2 = Convert.ToInt32(Console.ReadLine());

        int highestPowerOf2 = 0;
        int remainder = num2;
        while (remainder % 2 == 0) {
            highestPowerOf2++;
            remainder /= 2;
        }
        Console.WriteLine(highestPowerOf2);
    }
}

using System;

class MAIN {
    public static void Main(string[] args) {
        int a = Convert.ToInt32(Console.ReadLine());
        int b = Convert.ToInt32(Console.ReadLine());
        int c = Convert.ToInt32(Console.ReadLine());

        int max = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
        Console.WriteLine(max);
    }
}

using System;

class MAIN {
    public static void Main(string[] args) {
        int N = Convert.ToInt32(Console.ReadLine());

        if (N == 1) {
            Console.WriteLine(1);
        }
        for (int i = 0; i < N; i++) {
            if (i % 2 == 0) { 
                continue;
            }
            Console.WriteLine(i);
        }
    }
}

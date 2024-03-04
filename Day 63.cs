using System;

class MAIN  
{
    public static int addition(int a, int b)
    {
        return a + b;
    }

    public static void Main(string[] args) 
    {
        int a = Convert.ToInt32(Console.ReadLine());
        int b = Convert.ToInt32(Console.ReadLine());
        int sum = addition(a, b);
        Console.WriteLine(sum);
    }
}


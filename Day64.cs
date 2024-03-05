using System;

class MAIN {
    public static void func1(int val) {
        val = 2;
    }

    public static void func2(ref int val) {
        val = 2;
    }

    public static void Main(string[] args) {
        int val = Convert.ToInt32(Console.ReadLine());
        int a = 0, b = 0;
        func1(val);
        a = val;        
        func2(ref val);
        b = val;       
        
     
        bool isEqual = a == b;
        Console.WriteLine(isEqual);
    }
}

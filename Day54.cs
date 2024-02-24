using System;
using System.IO;

class MAIN  {
    public static void Main(string[] args) {
         int intValue;
        long longValue;
        char charValue;
        float floatValue;
        double doubleValue;

        // Prompt user to input values
        intValue = int.Parse(Console.ReadLine());
        longValue = long.Parse(Console.ReadLine());
        charValue = char.Parse(Console.ReadLine());
        floatValue = float.Parse(Console.ReadLine());
        doubleValue = double.Parse(Console.ReadLine());

        // Print the values
        Console.WriteLine(intValue);
        Console.WriteLine(longValue);
        Console.WriteLine(charValue);
        Console.WriteLine(floatValue);
        Console.WriteLine(doubleValue);
        
    }
}

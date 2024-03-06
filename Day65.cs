using System;
using System.IO;
using System.Text; // Include StringBuilder

class MAIN {
    public static void Main(string[] args) {
        // Declare a StringBuilder
        StringBuilder sb = new StringBuilder();

        // Append "Interview"
        sb.Append("Interview");

        // AppendLine "Bit"
        sb.AppendLine("Bit");

        // Append "C# Course"
        sb.Append("C# Course");

        // Print the current StringBuilder
        Console.WriteLine(sb);

        // Replace "Interview" with "C# "
        sb.Replace("Interview", "C# ");

        // Print the current StringBuilder
        Console.WriteLine(sb);

        // Print the length of the StringBuilder
        Console.WriteLine(sb.Length);
    }
}

using System;
using System.IO;

class MAIN
{
    public static void Main(string[] args)
    {
        // Use StreamReader to read from standard input (stdin)
        StreamReader reader = new StreamReader(Console.OpenStandardInput());

        // Use StreamWriter to write to standard output (stdout)
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        writer.AutoFlush = true; // Enable automatic flushing of the stream

        // Read input line by line until there's no more input
        string line;
        while ((line = reader.ReadLine()) != null)
        {
            // Process the input and write the output
            string output = ProcessInput(line);

            // Write the output to the standard output (stdout)
            writer.WriteLine(output);
        }
    }

    // Define a method to process input and return output
    static string ProcessInput(string input)
    {
        // Convert the first character of the input string to its ASCII value
        if (!string.IsNullOrEmpty(input))
        {
            char firstChar = input[0];
            int asciiValue = (int)firstChar;
            return asciiValue.ToString();
        }
        else
        {
            return "No input provided.";
        }
    }
}

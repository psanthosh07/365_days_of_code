/*
 using System;
using System.IO;

class MAIN  {
    public static void Main(string[] args) {
         int t = Convert.ToInt32(Console.ReadLine());
        
        for(int i=0;i<t;i++){
             string name = Console.ReadLine();
             int age = Convert.ToInt32(Console.ReadLine());
             int roll = Convert.ToInt32(Console.ReadLine());
             Student s1 = new Student();  
             s1.insert(name,age,roll);  
              
            s1.display(); 
         }
        
    }
}

*/
public class Student {
    // Member variables
    private string name;
    private int age;
    private int rollno;
    
    // Method to assign values to member variables
    public void insert(string n, int a, int r) {
        name = n;
        age = a;
        rollno = r;
    }
    
    // Method to display the values of member variables in a single line
    public void display() {
        Console.WriteLine(name + " " + age + " " + rollno);
    }
}

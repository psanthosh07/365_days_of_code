/*
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
*/

class Student{
    string name;
    int age;
    int rollno;
public:
 void set_variable(string newName, int newAge, int newRollNo) {
        name = newName;
        age = newAge;
        rollno = newRollNo;
    }

    // Function to print member variables
    void print_variable() {
        cout << name << endl;
        cout << age << endl;
        cout << rollno << endl;
    }
};

    // Create funtions here with the name given




/*
int main()  {
    Student obj1;
    obj1.set_variable("Robin", 15, 10);
    Student obj2;
    obj2.set_variable("Rahul", 20, 14);
    obj1.print_variable();
    obj2.print_variable();
    return 0;
}
*/

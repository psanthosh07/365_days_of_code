/*
#include<iostream>
using namespace std;
*/

// Your code goes here

class Animal {
protected:
    int age;
public:
    // Constructor
    Animal(int a) : age(a) {}

    // Virtual function for Eat()
    virtual void Eat() {
        cout << "Animal eats food" << endl;
    }

    // Function to get age
    int get_Age() {
        return age;
    }
};

// Derived class Dog
class Dog : public Animal {
public:
    // Constructor
    Dog(int a) : Animal(a) {}

    // Overridden function for Eat()
    void Eat() override {
        cout << "Dog eats meat" << endl;
    }

    // Overridden function for get_Age()
    int get_Age() {
        return age;
    }
};

// Derived class Cat
class Cat : public Animal {
public:
    // Constructor
    Cat(int a) : Animal(a) {}

    // Overridden function for Eat()
    void Eat() override {
        cout << "Cat eats meat" << endl;
    }

    // Overridden function for get_Age()
    int get_Age() {
        return age;
    }
};
/*
int main()  {
   Animal *a;
   Dog dg(8); //making object of child class Dog
   Cat ct(3); //making object of child class Cat
   
   a = &dg;
   a->Eat();
   cout << "Dog's age is: "<<a->get_Age()<<endl;
   a= &ct;
   a->Eat();
   cout << "Cat's age is: "<<a->get_Age()<<endl;
   return 0;
}
*/

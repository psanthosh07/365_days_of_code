/*
#include<iostream>
using namespace std;

int division(int a, int b) {
   if( b == 0 ) {
      throw "Division by zero condition!";
   }
   return (a/b);
}
*/

int main()  {
    int a, b;
    cin>>a>>b;
    try {
        double result = division(a,b);
        cout << result << endl;
    }
    catch (const char* message) {
        cout<< message << endl;
    }
    // call function division(a, b)
    // print the result in try else exception in catch
    // Your code goes here
    return 0;
}

/*
#include<iostream>
#include<sstream>
using namespace std;
*/

int main()  {
    string A;
    getline(cin, A); 
    stringstream ss(A);
    char delim = ',';
    string token;
    while (getline(ss, token, delim)) {
        cout << token << endl;
    }



    return 0;
}

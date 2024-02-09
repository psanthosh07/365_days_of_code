/*
#include<iostream>
#include<string>
using namespace std;
*/

int main() {
    string A, B;
    cin >> A >> B;
    int len1 = A.size();
    int len2 = B.size();
    string C = A + B;
    string D = A[0] + B.substr(1);
    string E = B[0] + A.substr(1);
    printf("%d %d\n", len1, len2);
    cout << A + B << endl;
    cout << E << " " << D << endl;

    return 0;
}

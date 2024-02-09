/*
#include <iostream>
using namespace std;
*/

// Your code goes here
template<class T>
int index_of_largest(T arr[], int size) {
    int index_of_largest = 0;
    for (int i = 1; i < size; ++i) {
        if (arr[i] > arr[index_of_largest]) {
            index_of_largest = i;
        }
    }
    return index_of_largest;
}




/*
int main()  {
    int n;
    cin>>n;
    int arr_int[n];
    for(int i = 0; i < n; i++){
        cin>>arr_int[i];
    }
    int res = index_of_largest<int>(arr_int, n);
    cout<<res<<endl;
    
    cin>>n;
    double arr_double[n];
    for(int i = 0; i < n; i++){
        cin>>arr_double[i];
    }
    res = index_of_largest<double>(arr_double, n);
    cout<<res<<endl;
    return 0;
}
*/

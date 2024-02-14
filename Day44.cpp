/*
#include <iostream>
#include <vector>
#include<tuple>
using namespace std;
*/

pair<int, int> findMaxMin(vector<int> &A){
     int maxNum = A[0];
    int minNum = A[0];
    
    for (int num : A) {
        maxNum = max(maxNum, num);
        minNum = min(minNum, num);
    }
    
    return make_pair(maxNum, minNum);
}

tuple<int, int, int> compute(vector<int> &A){

      int sum = 0;
    int evenSum = 0;
    int oddSum = 0;
    
    for (int num : A) {
        sum += num;
        if (num % 2 == 0) {
            evenSum += num;
        } else {
            oddSum += num;
        }
    }
    return make_tuple(sum, evenSum, oddSum);
}

/*
int main()  {
    int n;
    cin>>n;
    vector<int> A(n);
    for(int i = 0; i < n; i++){
        cin>>A[i];
    }
    
    pair<int, int> max_min = findMaxMin(A);
    cout<<max_min.first<<" "<<max_min.second<<endl;
    
    tuple<int, int, int> tuple_values = compute(A);
    cout<< get<0>(tuple_values) << " " << get<1>(tuple_values) << " " << get<2>(tuple_values) << endl;
    
    return 0;
}
*/

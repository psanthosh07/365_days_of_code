#include<iostream>
#include<vector>
#include<algorithm>
#include<iterator>
using namespace std;

int main()  {

     int N, Q;
    cin >> N;
    
    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }
    
    cin >> Q;
    while (Q--) {
        int X;
        cin >> X;
        
        auto lb = lower_bound(arr.begin(), arr.end(), X) - arr.begin();
        auto ub = upper_bound(arr.begin(), arr.end(), X) - arr.begin();
        
        if (arr[lb] == X) {
            cout << lb << endl;
        } else {
            cout << ub << endl;
        }
    }
    
    return 0;
}

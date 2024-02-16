/*
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
*/

// Complete the given function
vector<int> solve(vector<int> &A, int B){
     vector<int> result;
    deque<int> dq;

    // Process the first window separately
    for (int i = 0; i < B; ++i) {
        // Remove elements smaller than the current element from the back
        while (!dq.empty() && A[i] >= A[dq.back()]) {
            dq.pop_back();
        }
        dq.push_back(i);
    }

    // Process the remaining windows
    for (int i = B; i < A.size(); ++i) {
        // The front of the deque contains the index of the maximum element
        result.push_back(A[dq.front()]);

        // Remove elements that are out of the current window
        while (!dq.empty() && dq.front() <= i - B) {
            dq.pop_front();
        }

        // Remove elements smaller than the current element from the back
        while (!dq.empty() && A[i] >= A[dq.back()]) {
            dq.pop_back();
        }

        dq.push_back(i);
    }

    // Add the maximum element of the last window
    result.push_back(A[dq.front()]);

    return result;
}


/*
int main()  {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> A(n);
        for(int i = 0; i < n; i++){
            cin>>A[i];
        }
        int B;
        cin>>B;
        vector<int> ans = solve(A, B);
        for(int i = 0; i < ans.size(); i++){
            cout<<ans[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
*/

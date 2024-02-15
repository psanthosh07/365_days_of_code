#include <vector>
#include <algorithm>

using namespace std;

bool comp(pair<int, int> a, pair<int, int> b) { 
    // Compare pairs based on the sum of their elements
    return (a.first + a.second) < (b.first + b.second); 
}

void sortArray(vector<pair<int, int>>& A) {
    // Sort the array using the custom comparator
    sort(A.begin(), A.end(), comp);
}

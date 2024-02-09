/*
#include<iostream>
using namespace std;
*/

int main() {
    int N;
    cin>>N;
    // YOUR CODE GOES HERE
    int grid[N][N];

    // Fill the grid according to the specifications
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) {
                // Diagonal elements
                grid[i][j] = 0;
            } else if (i > j) {
                // Lower side
                grid[i][j] = -1;
            } else {
                // Upper side
                grid[i][j] = 1;
            }
        }
    }
    
    // Don't change the code below
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout<<grid[i][j]<<" ";
        }    
        cout<<endl;
    }
    return 0;
}

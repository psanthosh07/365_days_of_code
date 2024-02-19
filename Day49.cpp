#include<iostream>
#include<map>
using namespace std;

int main()  {
    int Q;
    cin >> Q;

    map<int, int> boxes;

    for (int i = 0; i < Q; ++i) {
        int type;
        cin >> type;

        if (type == 1) {
            int X, Y;
            cin >> X >> Y;
            boxes[X] += Y;
        } else if (type == 2) {
            int X;
            cin >> X;
            boxes[X] = 0; 
        } else if (type == 3) {
            int X;
            cin >> X;
            cout << boxes[X] << endl; 
        }
    }
    
    return 0;
}

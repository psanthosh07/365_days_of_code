#include<iostream>
#include<set>
#include<iterator>
using namespace std;

int main()  {
 int Q;
    cin >> Q;

    set<int> s;

    for (int i = 0; i < Q; ++i) {
        int y, x;
        cin >> y >> x;

        if (y == 1) {
            s.insert(x);
        } else if (y == 2) {
            s.erase(x);
        } else if (y == 3) {
            auto itr = s.find(x);
            if (itr != s.end()) {
                cout << "Yes" << endl;
            } else {
                cout << "No" << endl;
            }
        }
    }

    if (!s.empty()) {
        for (auto itr = s.begin(); itr != s.end(); ++itr) {
            cout << *itr << endl;
        }
    }

    return 0;
}

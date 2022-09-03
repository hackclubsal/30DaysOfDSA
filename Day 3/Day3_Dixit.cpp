#include <bits/stdc++.h>
using namespace std;
int main() {
    // int t; cin >> t;
    // while(t--) {
        
        
        int n,m; cin >> n >> m;
        int arr[n][m];
        
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                cin >> arr[i][j];
            }
        }

        
        int key; cin >> key;

        for (int i = 0; i < n ; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (arr[i][j] == key)
                {
                    cout << "Answer - true";
                    return 0;
                }
            }
        }

       
            cout << "Answer - false";


    // }
return 0;
}

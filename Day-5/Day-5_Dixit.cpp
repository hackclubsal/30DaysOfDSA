#include <bits/stdc++.h>
using namespace std;

int main()
{

    int n;
    cin >> n;
    vector<int> v(n);

    for (int i = 0; i < n; ++i)
    {
        cin >> v[i];
    }
    int xo = 0;
    for (int i = 0; i < n; ++i)
    {
        xo = xo ^ v[i];
    }

    cout << xo;

    return 0;
}

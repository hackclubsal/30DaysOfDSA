#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vi vector<int>
#define vl vector<ll>
#define pb push_back
// #define end '\n'
#define rep(i, a, b) for (int i = a; i < b; i++)
#define yes cout << "YES" << end
#define no cout << "NO" << end

void solve4()
{
    int n;
    cin >> n;
    map<char, int> m;
    for (int i = 0; i < n; ++i)
    {
        char a;
        cin >> a;
        m[a]++;
    }

    for (auto &p : m)
    {
        cout << p.first;
    }
}

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    // int tt; cin>>tt;
    // while(tt--)
    solve4();

    return 0;
}

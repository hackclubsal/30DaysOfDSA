#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vi vector<int>
#define vl vector<ll>
#define pb push_back
#define end '\n'
#define rep(i, a, b) for (int i = a; i < b; i++)
#define yes cout << "YES" << end
#define no cout << "NO" << end

int compareV(string s1, string s2)
{
    string temp1 = "", temp2 = "";
    int i = 0, j = 0;
    while (i < s1.size() || j < s2.size())
    {
        while (i < s1.size() && s1[i] == '0')
        {
            i++;
        }
        while (i < s1.size() && s1[i] != '.')
        {
            temp1 = temp1 + s1[i];
            i++;
        }
        while (j < s2.size() && s2[j] == '0')
        {
            j++;
        }
        while (j < s2.size() && s2[j] != '.')
        {
            temp2 = temp2 + s2[j];
            j++;
        }
        if (temp1.size() > temp2.size())
        {
            return 1;
        }
        else if (temp1.size() < temp2.size())
        {
            // cout << 1;
            return -1;
        }
        for (int k = 0; k < temp1.size(); k++)
        {
            if (temp1[k] > temp2[k])
            {
                return 1;
            }
            else if (temp1[k] < temp2[k])
            {
                // cout << 2;
                return -1;
            }
        }
        temp1 = "";
        temp2 = "";
        i++;
        j++;
    }
    return 0;
}
void solve()
{

    string s1, s2;
    cin >> s1 >> s2;
    cout << "Version 1: " << s1 << "\n"
         << "Version 2: " << s2 << "\n";
    // cout << compareV(s1,s2);
    cout << end;
    if (compareV(s1, s2) == 1)
    {
        cout << "Version 1 > Version 2";
    }
    else if (compareV(s1, s2) == -1)
    {
        cout << "Version 1 < Version 2";
    }
    else
        cout << "Version 1 = Version 2";
}

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    // int tt; cin>>tt;
    // while(tt--)
    solve();

    return 0;
}
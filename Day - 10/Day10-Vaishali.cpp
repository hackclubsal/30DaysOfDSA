#include <bits/stdc++.h>
using namespace std;

string removeDuplicateLetters(string s)
{
    vector<int> lastIndex(26, 0);
    for (int i = 0; i < s.length(); i++)
    {
        lastIndex[s[i] - 'a'] = i;
    }

    vector<bool> seen(26, false);
    stack<char> st;

    for (int i = 0; i < s.size(); i++)
    {
        int curr = s[i] - 'a';

        if (seen[curr])
        {
            continue;
        }

        while (st.size() > 0 && st.top() > s[i] && i < lastIndex[st.top() - 'a'])
        {
            seen[st.top() - 'a'] = false;
            st.pop();
        }
        st.push(s[i]);
        seen[curr] = true;
    }

    string res = "";
    while (st.size() > 0)
    {
        res += st.top();
        st.pop();
    }
    reverse(res.begin(), res.end());
    return res;
}

int main()
{
    string s;
    cout<<"Enter the string:"<<endl;
    cin>>s;

    cout<<removeDuplicateLetters(s);

    return 0;
}
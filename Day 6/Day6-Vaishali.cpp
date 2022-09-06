#include <bits/stdc++.h>
using namespace std;

void book(string s)
{
    int n = s.length();
    stack<char> st;
    for(int i=0; i<n; i++)
    {
        if(s[i]=='/' || (s[i]>='a' && s[i]<='z'))
            st.push(s[i]);

        else
        {
            string temp="";

            while(st.top()!='/')
            {
                temp += st.top();
                st.pop();
            }

            st.pop();

            for(int j=0; j<temp.length(); j++)
                st.push(temp[j]);
        }
    }

    string ans="";
    while(!st.empty())
    {
        ans += st.top();
        st.pop();
    }

    reverse(ans.begin(), ans.end());
    cout<<ans;
}

int main()
{
    string s;
    cout<<"Enter the string:"<<endl;
    cin >> s;

    book(s);

    return 0;
}
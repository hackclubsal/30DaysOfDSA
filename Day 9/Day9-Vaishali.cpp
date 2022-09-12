#include <bits/stdc++.h>
using namespace std;

int compareVersion(string version1, string version2)
{
    int vnum1 = 0, vnum2 = 0;

    for (int i = 0, j = 0; (i < version1.length() || j < version2.length());)
    {

        while (i < version1.length() && version1[i] != '.')
        {
            vnum1 = vnum1 * 10 + (version1[i] - '0');
            i++;
        }

        while (j < version2.length() && version2[j] != '.')
        {
            vnum2 = vnum2 * 10 + (version2[j] - '0');
            j++;
        }

        if (vnum1 > vnum2)
            return 1;
        if (vnum2 > vnum1)
            return -1;

        vnum1 = vnum2 = 0;
        i++;
        j++;
    }
    return 0;
}

int main()
{
    string s1, s2;
    cout<<"Enter first version string:"<<endl;
    cin>>s1;
    cout<<"Enter second version string:"<<endl;
    cin>>s2;    

    int flag = compareVersion(s1, s2);

    if(flag == 1)
        cout<<"Version 1 is greater";
    else if(flag == -1)
        cout<<"Version 2 is greater";
    else
        cout<<"Both are equal";
        
    return 0;
}
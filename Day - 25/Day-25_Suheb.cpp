#include <bits/stdc++.h>
using namespace std;

int isSubstring(string s1, string s2){

    if (s1.find(s2) != string::npos)
    return s1.find(s2);

    return -1;
}

int main(){

    string s1 = "helloworld";
    string s2 = "low";

    int res = isSubstring(s1, s2);
    cout << res;

    return 0;
}


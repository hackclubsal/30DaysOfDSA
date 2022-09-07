#include <bits/stdc++.h>
using namespace std;

bool isPerfectSquare(int n)
{
    if (n == 0 || n==1){
        return true;
    }
    int i = 1;
    while(n>=i*i)
    {
        if (n%i == 0 && n/i == i){
            return true;
        }
        i++;
    }
    return false;
}

int main() {
    int n; cin >> n;
    if(isPerfectSquare(n)){
        cout << "true";
    }
    else {
        cout << "false";
    }
    return 0;
}

#include <bits/stdc++.h>
using namespace std;

bool isPerfectSquare(int num)
{
    long long low = 1, high = num;

    while (low <= high)
    {
        long long mid = (low + high) / 2;
        long long sqaure = mid * mid;

        if (sqaure == num)
            return true;
        else if (sqaure > num)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return false;
}

int main()
{
    int n;
    cout<<"Enter the number:"<<endl;
    cin>>n;

    bool flag = isPerfectSquare(n);

    if(flag)
        cout<<"true";
    else
        cout<<"false";

    return 0;
}
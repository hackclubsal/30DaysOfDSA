#include<bits/stdc++.h>
using namespace std;

int main()
{
    int a[]={1,0,1,0,1,0,0,1};
    int n=sizeof(a)/sizeof(int);
    sort(a,a+n);
    cout<<"Array after sorting"<<endl;
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
    return 0;
}
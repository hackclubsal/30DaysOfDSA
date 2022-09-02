#include <iostream>
using namespace std;

void rotate(int arr[], int k, int n)
{
    k = k%n;
    
    for(int i=0; i<n; i++)
    {
        if(i<k)
        {
            cout<<arr[n+i-k]<<" ";
        }
        else
            cout<<arr[i-k]<<" ";
    }
}

int main()
{
    int n,k;
    cin>>n;
    int arr[n];
    for(int i=0; i<n; i++)
        cin>>arr[i];

    cin>>k;

    rotate(arr, k, n);

    return 0;
}
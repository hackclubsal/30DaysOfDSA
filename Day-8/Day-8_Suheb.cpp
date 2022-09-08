#include <bits/stdc++.h>
using namespace std;
 
int kadane(int arr[], int n)
{
    int maxSoFar = 0;
 
    int maxEndingHere = 0;
 
    for (int i = 0; i < n; i++)
    {
        maxEndingHere = maxEndingHere + arr[i];
        maxEndingHere = max(maxEndingHere, 0);
        maxSoFar = max(maxSoFar, maxEndingHere);
    }
 
    return maxSoFar;
}
 
int main()
{
    int arr[] = {-2,1,-3,4,-1,2,1,-5,4};
    int n = sizeof(arr)/sizeof(arr[0]);
 
    cout << "The maximum sum of a contiguous subarray is " << kadane(arr, n);
 
    return 0;
}

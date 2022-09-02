#include <bits/stdc++.h>
using namespace std;

void rightRotate(int a[], int n, int k)
{
    k = k % n;
 
    for(int i = 0; i < n; i++)
    {
       if(i < k)
       {
           cout << a[n + i - k] << " ";
       }
       else
       {
           cout << (a[i - k]) << " ";
       }
    }
    cout << "\n";
}

int main()
{
	int nums[] = { 1, 2, 3, 4, 5, 6, 7 };
	int n = sizeof(nums) / sizeof(nums[0]);

	int k;
    cout<<"Enter the value of k\n";
    cin>>k;

	rightRotate(nums,n,k);

	return 0;
}

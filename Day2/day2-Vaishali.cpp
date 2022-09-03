#include <iostream>
#include<bits/stdc++.h>
using namespace std;

void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k%n;
        int low=n-k, high=n-1;
        while(low<high)
        {
            swap(nums[low++], nums[high--]);
        }
        
        int low1=0, high1=n-k-1;
        while(low1<high1)
        {
            swap(nums[low1++], nums[high1--]);
        }
        
        int low2=0, high2=n-1;
        while(low2<high2)
        {
            swap(nums[low2++], nums[high2--]);
        }
    }

int main()
{
    int n,k,a;
    cin>>n;
    vector<int> nums;
    for(int i=0; i<n; i++)
    {
        cin>>a;
        nums.push_back(a);
    }    

    cin>>k;

    rotate(nums, k);

    for(auto x : nums)
        cout<<x<<" ";

    return 0;
}
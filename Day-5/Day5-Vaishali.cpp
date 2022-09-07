#include <bits/stdc++.h>
using namespace std;

int singleNonDuplicate(vector<int> &nums)
{
    int n = nums.size();
    int low = 0, high = n - 1;

    if (n == 1)
        return nums[0];

    if (nums[low] != nums[low + 1])
        return nums[low];

    if (nums[high] != nums[high - 1])
        return nums[high];

    while (low <= high)
    {
        int mid = (low + high) / 2;

        if (nums[mid] != nums[mid + 1] && nums[mid] != nums[mid - 1])
            return nums[mid];

        else if ((mid % 2 == 0 && nums[mid] != nums[mid + 1]) || (mid % 2 != 0 && nums[mid] != nums[mid - 1]))
            high = mid - 1;

        else
            low = mid + 1;
    }
    return -1;
}

int main()
{
    int n,a;
    cout<<"Enter the size of array:"<<endl;
    cin>>n;
    vector<int>nums;
    cout<<"Enter the elements:"<<endl;
    for(int i=0; i<n; i++)
    {
        cin>>a;
        nums.push_back(a);
    }

    cout<<singleNonDuplicate(nums);
    return 0;
}
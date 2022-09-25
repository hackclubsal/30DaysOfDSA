#include <bits/stdc++.h>
using namespace std;

int maxSubArray(vector<int> &nums)
{
    int sum = INT_MIN, currSum = 0, n = nums.size();

    for (int i = 0; i < n; i++)
    {
        currSum += nums[i];
        sum = max(currSum, sum);

        if (currSum < 0)
            currSum = 0;
    }

    return sum;
}

int main()
{
    int n, a;
    cout << "Enter number of Elements:" << endl;
    cin >> n;

    vector<int> nums;
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        nums.push_back(a);
    }

    int sum = maxSubArray(nums);
    cout << "Maximum Sum of Contiguous Array:" << sum;
    
    return 0;
}
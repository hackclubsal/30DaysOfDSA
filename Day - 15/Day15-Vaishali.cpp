#include <bits/stdc++.h>
using namespace std;

vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
{
    vector<int> ans;
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
    int n1 = nums1.size(), n2 = nums2.size();
    int i = 0, j = 0, k = 0;

    while (i < n1 && j < n2)
    {
        if (nums1[i] == nums2[j])
        {
            if (k != 0 && nums1[i] == ans[k - 1])
            {
                i++;
                j++;
            }
            else
            {
                ans.push_back(nums1[i]);
                i++;
                j++;
                k++;
            }
        }
        else if (nums1[i] > nums2[j])
            j++;
        else
            i++;
    }
    return ans;
}

int main()
{
    int n1,a,n2;
    vector<int> nums1, nums2;
    cout<<"Enter number of elements in first array: ";
    cin>>n1;
    cout<<"Enter Elements of first array: ";
    for(int i=0; i<n1; i++)
    {
        cin>>a;
        nums1.push_back(a);
    }

    cout<<"Enter number of elements in second array: ";
    cin>>n2;
    cout<<"Enter Elements of second array: ";
    for(int i=0; i<n2; i++)
    {
        cin>>a;
        nums2.push_back(a);
    }

    vector<int> ans =intersection(nums1, nums2);
    for(auto x : ans)
        cout<<x<<" ";

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

vector<int> countDistinct(int A[], int n, int k)
{
    vector<int> ans;
    unordered_map<int, int> mp;
    int count = 0;
    for (int j = 0; j < k; j++)
    {
        if (mp[A[j]] == 0)
            count++;
        mp[A[j]]++;
    }
    ans.push_back(count);
    for (int i = k; i < n; i++)
    {
        if (mp[A[i - k]] == 1)
            count--;

        mp[A[i - k]]--;
        if (mp[A[i]] == 0)
            count++;
        mp[A[i]]++;
        ans.push_back(count);
    }
    return ans;
}

int main()
{
    int n, k;
    cout << "Enter number of elements: ";
    cin >> n;
    cout << "Enter the window size: ";
    cin >> k;
    cout<<"Enter elements: ";
    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    vector<int> ans = countDistinct(arr, n, k);
    for (int i = 0; i < ans.size(); i++)
        cout << ans[i] << " ";

    return 0;
}
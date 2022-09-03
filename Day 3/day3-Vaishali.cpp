#include<bits/stdc++.h>
using namespace std;

bool searchMatrix(vector<vector<int>> &matrix, int target)
{
    int row = matrix.size(), col = matrix[0].size();
    int low = 0, high = (row * col) - 1;

    while (low <= high)
    {
        int middle = (low + high) / 2;

        if (matrix[middle / col][middle % col] == target)
            return true;
        else if (matrix[middle / col][middle % col] > target)
            high = middle - 1;
        else
            low = middle + 1;
    }
    return false;
}

int main()
{
    int n,m,a,target;
    cin>>n>>m;
    vector<vector<int>> nums;
    for(int i=0; i<n; i++)
    {
        vector<int>temp;
        for(int j=0; j<m; j++)
        {
            cin>>a;
            temp.push_back(a);
        }
        nums.push_back(temp);
        temp.clear();
    }
    cin>>target;

    cout<<searchMatrix(nums, target);

    return 0;
}
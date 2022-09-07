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
    cout<<"Enter number of rows:"<<endl;
    cin>>n;
    cout<<"Enter number of cols:"<<endl;
    cin>>m;
    cout<<"Enter elements of matrix:"<<endl;
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
    cout<<"Enter target value:"<<endl;
    cin>>target;

    if(searchMatrix(nums, target))
        cout<<"true";
    else
        cout<<"false";

    return 0;
}
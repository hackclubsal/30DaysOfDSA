#include<bits/stdc++.h>
using namespace std;
bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        int m = matrix[0].size();
        int row = 0;
        int col = m-1;
        while(row<n && col>-1){
            int cur = matrix[row][col];
            if(cur==target) return true;
            if(target <cur){
                col--;
            }
            else{
                row++;   
            }
        }
        return false;
}
int main(){
    vector<vector<int>> matrix = {{1,2,3},{4,5,6},{7,8,9}};
    bool flag = false;
    flag = searchMatrix(matrix, 10);
    if(flag ==true){
        cout<<"True"<<endl;
    }
    else{
        cout<<"False"<<endl;
    }
    
}
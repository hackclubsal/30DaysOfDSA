#include<bits/stdc++.h>
using namespace std;
int main(){
    int a[]={ 1, 0, 1, 0, 1, 0, 0, 1 };
    int n=8;
    int count=0,count2=0;
    for(int i=0;i<n;i++){
        if(a[i]==0){
            count++;
        }
        else count2++;
    }
    for(int i=0;i<count;i++){
        a[i]=0;
    }
    for(int i=count2;i<n;i++){
        a[i]=1;
    }
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
    return 0;
}

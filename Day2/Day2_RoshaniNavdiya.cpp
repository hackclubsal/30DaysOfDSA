//Code by Roshani Navdiya
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cout<<"Enter the number of elements in array";
    cin>>n;
    int a[n];
    cout<<"Enter elements of array";
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int k;
    cout<<"Enter the number of rotation";
    cin>>k;
    int ans[n];
    int l=k;
    //Last k elements are shifted first
    cout<<l<<endl;
    for(int i=0;i<k;i++){
        ans[i]=a[n-l];
        l--;
    }
    int j=0;
    //Onther elements are behind the first k elements
    for(int i=k;i<n;i++){
        ans[i] = a[j];
        j++;
    }
    //Ans array
    for(int i=0;i<n;i++){
        cout<<ans[i]<<" ";
    }
}
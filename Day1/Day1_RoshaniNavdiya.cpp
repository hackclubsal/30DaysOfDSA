// Code by Roshani Navdiya
#include<bits/stdc++.h>
using namespace std;
void sortBinaryArray(int a[],int n);
int main(){
    int n;
    cout<<"Enter the number of binary element in array:"<<endl;
    cin>>n;
    int a[n];
    cout<<"Enter elements of array:"<<endl;
    for(int i=0;i<n;i++){
        
        cin>>a[i];
    }
    sortBinaryArray(a,n);
    cout<<"Sorted Array:"<<endl;
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
}
void sortBinaryArray(int a[],int n){
    int zeros = 0;
    //Find the number of zeros in array and increase the counter "zeros".
    for(int i=0;i<n;i++){
        if(a[i]==0){
            zeros++;
        }
    }
    //Make/Put all zeros in starting of the array.
    for(int i=0;i<zeros;i++){
        a[i]=0;
    }
    //Make all one after the all zeros
    for(int i=zeros;i<n;i++){
        a[i]=1;
    }
}
#include<iostream>
using namespace std;

void binarysort(int a[], int n){
	int k = -1;
	for(int i=1;i<n;i++){
		if(a[i]<1){
			k++;
			swap(a[i],a[k]);
		}
	}
}

int main(){
	int a[] ={ 1, 0, 1, 0, 1, 0, 0, 1 
	};
	int n = sizeof(a) / sizeof(a[0]);
	binarysort(a,n);
	for(int i=0;i<n;i++){
		cout<<a[i]<<" ";
	}
	return 0;
}

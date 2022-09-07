#include <bits/stdc++.h>
using namespace std;

bool isPerfectSquare(int n)
{
	for (int sum = 0, i = 1; sum < n; i += 2) {
		sum += i;
		if (sum == n)
			return true;
	}
	return false;
}

int main()
{
    int num;
    cout<<"Enter the number to check: "<<endl;
    cin>>num;

    if(isPerfectSquare(num)){
        cout<<"True";
    }
    else{
        cout<<"False";
    }
	return 0;
}

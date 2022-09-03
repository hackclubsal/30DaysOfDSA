#include <bits/stdc++.h>
using namespace std;

#define N 3
#define M 3

bool binarySearch1D(int arr[], int K)
{
	int low = 0;
	int high = N - 1;
	while (low <= high) {
		int mid = low + (high - low) / 2;

		if (arr[mid] == K)
			return true;

		if (arr[mid] < K)
			low = mid + 1;
		else
			high = mid - 1;
	}

	return false;
}

bool searchMatrix(int matrix[N][M], int K)
{
	int low = 0;
	int high = M - 1;
	while (low <= high) {
		int mid = low + (high - low) / 2;

		if (K >= matrix[mid][0]
			&& K <= matrix[mid][M - 1])
			return binarySearch1D(matrix[mid], K);

		if (K < matrix[mid][0])
			high = mid - 1;
		else
			low = mid + 1;
	}

	return false;
}

int main()
{
	int matrix[N][M] = { { 1, 2, 3},
						{ 4, 5, 6},
						{ 7, 8, 9} };
	int K;
    cout<<"Enter the key value to search: "<<endl;
    cin>>K;
	if (searchMatrix(matrix, K))
		cout << "True" << endl;
	else
		cout << "False" << endl;
}

#include <bits/stdc++.h>
using namespace std;
#define N 3

void rotateMatrix(int mat[][N]){ 

	for (int i = 0; i < N; i++)
		reverse(mat[i], mat[i] + N);

	for (int i = 0; i < N; i++) {
		for (int j = i; j < N; j++)
			swap(mat[i][j], mat[j][i]);
	}
}

void displayMatrix(int mat[N][N]){

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << mat[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

int main()
{
	int mat[N][N] = { { 1, 2, 3 },
					{ 4, 5, 6 },
					{ 7, 8, 9 }};

	rotateMatrix(mat);

	displayMatrix(mat);

	return 0;
}

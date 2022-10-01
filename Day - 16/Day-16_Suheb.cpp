#include<bits/stdc++.h>
using namespace std;

int minDiff;
void getPartition(vector<int> &A, int selectedStudents, int start, int currSum, int totalSum) {
	if (start == A.size()) {
		return;
	}
	if (selectedStudents == A.size()/2) {
		minDiff = min(minDiff, abs(totalSum - 2 * currSum));
		return;
	}
	getPartition(A, selectedStudents + 1, start + 1, currSum + A[start], totalSum);
	getPartition(A, selectedStudents, start + 1, currSum, totalSum);
}
int divideGroup(vector<int> &A) {
	int totalSum = 0;
	for (int i = 0; i < A.size(); i++) {
		totalSum += A[i];
	}
	minDiff = INT_MAX;
	getPartition(A, 0, 0, 0, totalSum);
	return minDiff;
}
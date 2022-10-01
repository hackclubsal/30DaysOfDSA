#include <bits/stdc++.h>
using namespace std;

void countDistinct(int A[], int K, int N)
{
	unordered_map<int, int> hashMap;

	int distCount = 0;

	for (int i = 0; i < K; i++) {

		if (hashMap[A[i]] == 0) {
			distCount++;
		}
		hashMap[A[i]] += 1;
	}

	cout << distCount << ' ';

	for (int i = K; i < N; i++) {

		if (hashMap[A[i - K]] == 1) {
			distCount--;
		}

		hashMap[A[i - K]] -= 1;

		if (hashMap[A[i]] == 0) {
			distCount++;
		}

		hashMap[A[i]] += 1;
		cout << distCount << ' ';
	}
}

int main()
{
	int A[] = {4,1,1};
	int N = sizeof(A) / sizeof(A[0]);
	int K = 2;

	countDistinct(A, K, N);

	return 0;
}

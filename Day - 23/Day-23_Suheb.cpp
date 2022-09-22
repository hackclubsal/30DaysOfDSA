#include <bits/stdc++.h>
using namespace std;

void printKMax(int A[], int N, int K){

    std::deque<int> Qi(K);

    int i;
    for (i = 0; i < K; ++i) {

        while ((!Qi.empty()) && A[i] >= A[Qi.back()])
            Qi.pop_back();

    Qi.push_back(i);
    
    }

    for (; i < N; ++i) {

        cout << A[Qi.front()] << " ";

        while ((!Qi.empty()) && Qi.front() <= i - K)
            Qi.pop_front();

        while ((!Qi.empty()) && A[i] >= A[Qi.back()])
            Qi.pop_back();

    Qi.push_back(i);

    }
    cout << A[Qi.front()];

}

int main()
{
    int A[] = {1, -2, 3, 4, 5, 3, 4, -1};
    int N = sizeof(A) / sizeof(A[0]);
    int K = 3;

    printKMax(A, N, K);
    return 0;
}

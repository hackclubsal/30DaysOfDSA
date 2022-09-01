#include <bits/stdc++.h>
using namespace std;

void binSort(int A[], int N)
{
    int j = -1;

    for (int i = 0; i < N; i++)
    {
        if (A[i] == 0)
        {
            j++;
            swap(A[i], A[j]);
        }
    }
}

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        int N;
        cin >> N;
        int A[N];

        for (int i = 0; i < N; i++)
            cin >> A[i];

        binSort(A, N);

        for (int x : A)
            cout << x << " ";
    }
    return 0;
}
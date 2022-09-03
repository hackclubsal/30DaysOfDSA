#include <bits/stdc++.h>
using namespace std;
void right_rotate(int a[], int n, int k)
{
    k = k % n;

    for (int i = 0; i < n; i++)
        cout << a[(n - k + i) % n]<<" ";
}
int main()
{
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(a) / sizeof(int);
    int k;
    cout << "Enter number of steps" << endl;
    cin >> k;
    right_rotate(a, n, k);
    return 0;
}
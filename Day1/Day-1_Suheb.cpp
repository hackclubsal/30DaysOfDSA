#include <bits/stdc++.h>
using namespace std;
 
void swap(int A[], int i, int j)
{
    int temp = A[i]; 
    A[i] = A[j];
    A[j] = temp;
}
 
int split(int A[], int n)
{
    int pivot = 1;
    int j = 0;

    for (int i = 0; i < n; i++)
    {
        if (A[i] < pivot)
        {
            swap(A, i, j);
            j++;
        }
    }
}
 
int main(void)
{
    int A[] = { 1, 0, 1, 0, 1, 0, 0, 1 };
    int n = sizeof(A)/sizeof(A[0]);
 
    split(A, n);
    
    for (int i = 0; i < n; i++) {
        printf("%d ", A[i]);
    }
 
    return 0;
}
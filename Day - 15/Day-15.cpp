#include <bits/stdc++.h>
using namespace std;

void intersection(int arr1[], int arr2[], int m, int n)
{
 int i = 0, j = 0;
 while (i < m && j < n) {
  if (arr1[i] < arr2[j])
   i++;
  else if (arr2[j] < arr1[i])
   j++;
  else 
  {
   cout << arr2[j] << " ";
   i++;
   j++;
  }
 }
}

int main()
{
 int arr1[] = {1, 3, 4, 5, 5, 6, 6, 7};
 int arr2[] = {2, 5, 6, 6, 7, 8};

 int m = sizeof(arr1) / sizeof(arr1[0]);
 int n = sizeof(arr2) / sizeof(arr2[0]);

 intersection(arr1, arr2, m, n);

 return 0;
}

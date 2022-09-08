#include <bits/stdc++.h>
using namespace std;

long maxArraySum(int arr[], int n)
{
   long sum1 = 0;
   long sum2 = 0;

   for(int i=0;i<n;i++) {
         sum1+=arr[i];
         if(sum1>=sum2) {
            sum2=sum1;
         }
         if(sum1<0) {
            sum1=0;
            continue;
         }
      }
      return sum2;
}

int main() {

   int arr[] = {-2,1,-3,4,-1,2,1,-5,4};
   long ans = maxArraySum(arr,9);
   cout << ans << "\n";



return 0;
}
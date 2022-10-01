#include <bits/stdc++.h>
using namespace std;

int minOp(string s1, string s2, int n, int m,
  vector<vector<int> >& dp)
{

 if (n == 0){
    return m;
 }

 if (m == 0){
    return n;
 }

 if (dp[n][m] != -1){
    return dp[n][m];
 }

 if (s1[n - 1] == s2[m - 1]) {
  return dp[n][m] = minOp(s1, s2, n - 1, m - 1, dp);
 }
 
 else {
  int insert, del, replace; 

  insert = minOp(s1, s2, n, m - 1, dp);
  del = minOp(s1, s2, n - 1, m, dp);
  replace = minOp(s1, s2, n - 1, m - 1, dp);
  return dp[n][m] = 1 + min(insert, min(del, replace));
 }
}

int main()
{

 string s1 = "hello";
 string s2 = "seldom";

 int n = s1.length(), m = s2.length();
 vector<vector<int> > dp(n + 1, vector<int>(m + 1, -1));

 cout << minOp(s1, s2, n, m, dp);
 return 0;

}

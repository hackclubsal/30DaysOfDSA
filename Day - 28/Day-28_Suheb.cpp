#include <bits/stdc++.h>
using namespace std;

int minCuts(string s)
{
	int cut[s.length()];
	bool palindrome[s.length()][s.length()];
	memset(palindrome, false, sizeof(palindrome));
	for (int i = 0; i < s.length(); i++)
	{
		int minCuts = i;
		for (int j = 0; j <= i; j++)
		{
			if (s[i] == s[j] && (i - j < 2 || palindrome[j + 1][i - 1]))
			{
				palindrome[j][i] = true;
				minCuts = min(minCuts, j == 0 ? 0 : (cut[j - 1] + 1));
			}
		}
		cut[i] = minCuts;
	}
	return cut[s.length() - 1];
}

int main()
{
	cout << minCuts("aabc") << endl;
	return 0;
}


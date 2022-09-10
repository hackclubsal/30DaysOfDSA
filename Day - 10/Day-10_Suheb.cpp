#include <bits/stdc++.h>
using namespace std;

string removeDuplicate(string s)
{
	int count[26] = { 0 };

	int visChar[26] = { 0 };

	int n = s.size();

	for (int i = 0; i < n; i++)
		count[s[i] - 'a']++;

	string res = "";

	for (int i = 0; i < n; i++) {

		count[s[i] - 'a']--;

		if (!visChar[s[i] - 'a']) {

			while (res.size() > 0
				&& res.back() > s[i]
				&& count[res.back() - 'a'] > 0) {

				visChar[res.back() - 'a'] = 0;
				res.pop_back();
			}

			res += s[i];
			visChar[s[i] - 'a'] = 1;
		}
	}
	return res;
}

int main()
{
	string S = "cbacdcbc";

	cout << removeDuplicate(S);

	return 0;
}

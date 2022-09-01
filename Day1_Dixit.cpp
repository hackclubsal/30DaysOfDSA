#include <bits/stdc++.h>
using namespace std;
int main() {
	// int t; cin >> t;
	// while(t--) {
		
		int n; cin >> n;
		vector <int> v(n);

		for (int i = 0; i < n ; ++i)
		{
			cin >> v[i];
		}

		int cnt = count(v.begin(), v.end(), 0);

		for (int i = 0; i < cnt; ++i)
		{
			cout << 0 << " ";
		}
		for (int i = 0; i < n-cnt; ++i)
		{
			cout << 1 << " ";
		}



	// }
return 0;
}

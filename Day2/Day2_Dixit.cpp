#include <bits/stdc++.h>
using namespace std;
int main() {
	// int t; cin >> t;
	// while(t--) {
		
		int n,y=0; cin >> n;
		int k; cin >> k;
		
		deque<int> dq;

		for (int i = 0; i < n; ++i)
		{
			int x; cin >> x;
			dq.push_back(x);
		}

		while(k--)
		{
			int y = dq.back();
			dq.push_front(y);
			dq.pop_back();
		}

		for(auto& i:dq)
		{
			cout<<i<<" ";
		}

	// }
return 0;
}

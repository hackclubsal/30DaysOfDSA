#include <bits/stdc++.h>
using namespace std;

vector<string> orderReviews(vector<string> &reviews, vector<string> &gW) {

    set<string> words(gW.begin(), gW.end());
	int n = reviews.size();
	pair<int, int> g[n];
	vector<string> res(n);

	for (int i = 0; i < n; i++) {

		string review = reviews[i];
		int m = review.length();
		int numgW = 0;
		int s = 0;

		for (int j = 0; j < m; j++) {

			if (review[j] == ' ') {

				if (words.find(review.substr(s, j - s)) != words.end()) {
					numgW++;

				}
				s = j + 1;

			}

		}
		if (words.find(review.substr(s)) != words.end()) {
			numgW++;

		}
		pair<int, int> gi = {numgW, i};
		g[i] = gi;
	}

	sort(g, g + n, [&] (pair<int, int> &p1, pair<int, int> &p2) {

		if(p1.first < p2.first) {
			return p1.first < p2.first;
		}
		
		else {
			if(p1.first == p2.first) {
				return p1.second >= p2.second;
			}

			else {
				return p1.first < p2.first;
			}
		}
	});

	reverse(g, g + n);

	for (int i = 0; i < n; i++) {

		res[i] = reviews[g[i].second];

	}
	return res;

}
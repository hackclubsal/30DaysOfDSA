#include<bits/stdc++.h>
using namespace std;

vector<int> possibleList;
bool isPossible;
void solve(string c,int start,int n){
	if(start == n) {
		for(int i = 1; i < possibleList.size(); i++) {
			if(possibleList[i - 1] - 1 == possibleList[i]) {
				continue;
			}
			isPossible = false;
			return;
		}
		if(possibleList.size() != 1) {
			isPossible = true;
		}
		return;
	}

	int num = 0;
	for(int i = start; i < n; i++){
		num = num * 10 + (c[i] - '0');
		possibleList.push_back(num);
		solve(c, i + 1, n);
		if(isPossible){
			return;
		}
		possibleList.pop_back();
	}
}

bool isConsecutivelyDescending(string s) {
	possibleList.clear();
	isPossible = false;
	solve(s, 0, s.length());
	return isPossible;
}
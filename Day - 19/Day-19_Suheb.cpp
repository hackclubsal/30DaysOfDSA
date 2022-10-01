#include<bits/stdc++.h>
using namespace std;

bool wordBreakUtil(string s, int start, vector<string> &w) {
	if (start == s.size()) {
		return true;
	}
	for (int i = start; i < s.size(); i++) {
		string currWord = s.substr(start, i - start + 1);
		for(int j = 0; j < w.size(); j++) {
			if (currWord == w[j]) {
				if(wordBreakUtil(s, i + 1, w)) {
					return true;
				}
			}
		}
	}
	return false;
}

bool wordBreak (string s, vector<string> &w) {
    return wordBreakUtil(s, 0, w);
}

int main(){
    string s = "workattech";
    vector<string> w = {"tech", "work", "problem", "at"};
    bool res = wordBreak(s,w);

    cout<<boolalpha<<res;

    return 0;

}
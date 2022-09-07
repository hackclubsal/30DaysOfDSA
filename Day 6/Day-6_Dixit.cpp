#include <bits/stdc++.h>
using namespace std;
int main() {
	string s;
	cin >> s;
	
	stack<string> st;
	//intially assume current string empty
	string curr_s = "";
	for(int i = 0; i < (int)s.size(); i++) {
	//if somewhere u find '(' store curr_s into stack
		if(s[i] == '/') {
			st.push(curr_s);
			curr_s = "";
		} else if(s[i] == '\\') {
			reverse(curr_s.begin(), curr_s.end());
			string top = st.top();
			st.pop();
			top.append(curr_s);
			curr_s = top;
		} else {
			curr_s.push_back(s[i]);
		}
	}
	//return the curr_s
	cout <<  curr_s << endl;

	
        	
return 0; 
}
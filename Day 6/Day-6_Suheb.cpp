#include <bits/stdc++.h>
using namespace std;

const int N = 100001;
string s;
vector<char> ans;

void handle(int left, int right) {
  while (left < right) {
    swap(s[left++], s[right--]);
  }
}

int main() {
  cin >> s;
  stack<int> sh;
  for (int i = 0; i < s.length(); i++) {
    if (s[i] == '/') {
      sh.push(i);
    }
    if (s[i] == '\\') {
      handle(sh.top(), i);
      sh.pop();
    }
  }
  for (int i = 0; i < s.length(); i++) {
      if (s[i] == '/') {
        continue;
      }
      if (s[i] == '\\') {
        continue;
      }
      cout << s[i];
    }
    cout << endl;

  return 0;
}


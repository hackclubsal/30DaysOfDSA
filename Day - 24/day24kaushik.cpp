#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define MAX 26


bool cmp(const pair<int, int>& a, const pair<int, int>& b)
{


    if (a.F == b.F)
        return a.S < b.S;
    return a.F > b.F;
}


struct node {
    bool exist;
    node* arr[MAX];
    node(bool bul = false)
    {
        exist = bul;
        for (int i = 0; i < MAX; i++)
            arr[i] = NULL;
    }
};


void add(string s, node* trie)
{
    // Add a node to the trie
    int n = s.size();
    for (int i = 0; i < n; i++) {



        if (trie->arr[s[i] - 'a'] == NULL)
            trie->arr[s[i] - 'a'] = new node();

        trie = trie->arr[s[i] - 'a'];
    }
    trie->exist = true;
    return;
}



bool search(string s, node* trie)
{

    for (int i = 0; i < s.size(); i++) {
        if (trie->arr[s[i] - 'a'] == NULL)
            return false;

        trie = trie->arr[s[i] - 'a'];
    }
    return trie->exist;
}



void convert(string& str)
{

    for (int i = 0; i < str.size(); i++)
        if (str[i] == '_')
            str[i] = ' ';
    return;
}


void sortArr(string good, vector<string>& review)
{



    convert(good);
    node* trie = new node();
    string word;
    stringstream ss;
    ss << good;



    while (ss >> word)
        add(word, trie);
    int k, n = review.size();



    vector<pair<int, int> > rating(n);
    for (int i = 0; i < n; i++) {
        convert(review[i]);
        ss.clear();
        ss << review[i];
        k = 0;
        while (ss >> word) {



            if (search(word, trie))
                k++;
        }




        rating[i].F = k;
        rating[i].S = i;
    }



    sort(rating.begin(), rating.end(), cmp);


    for (int i = 0; i < n; i++)
        cout << review[rating[i].S] << "\n";
}


int main()
{


    string S = "this_is_good_as_well_as_tasty_food_restaurant";


    vector<string> R = { "good", "lovely",
                         "tasty", "nice" };


    sortArr(S, R);
}
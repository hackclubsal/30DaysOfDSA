#include<bits/stdc++.h>
using namespace std;

class JewelStone {
public:
   int weight, value;
   JewelStone(int weight, int value) {
       this->weight = weight;
       this->value = value;
   }
};

int knapSack(vector<JewelStone*> &stones, int capacity, int n) {
   if(n == 0 || capacity == 0) {
       return 0;
   }
   if(stones[n - 1]->weight > capacity) {
       return knapSack(stones, capacity, n - 1);
   }
   return max(stones[n - 1]->value + knapSack(stones, capacity - stones[n - 1]->weight, n - 1), knapSack(stones, capacity, n - 1));
}

int getMaxValue(vector<JewelStone*> stones, int capacity) {
   return knapSack(stones, capacity, stones.size());
}
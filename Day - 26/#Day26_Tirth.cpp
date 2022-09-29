class JewelStone {
public:
   int weight, value;
   JewelStone(int weight, int value) {
       this->weight = weight;
       this->value = value;
   }
};
*/
int getMaxValue(vector<JewelStone*> stones, int capacity) {
   int dp[stones.size() + 1][capacity + 1];
   for(int i = 0; i <= stones.size(); i++) {
       for(int j = 0; j <= capacity; j++) {
           if(i == 0 || j == 0) {
               dp[i][j] = 0;
           } else if(j - stones[i - 1]->weight >= 0) {
               dp[i][j] = max(dp[i - 1][j - stones[i - 1]->weight] + stones[i - 1]->value, dp[i - 1][j]);
           } else {
               dp[i][j] = dp[i - 1][j];
           }
       }
   }
   return dp[stones.size()][capacity];
}

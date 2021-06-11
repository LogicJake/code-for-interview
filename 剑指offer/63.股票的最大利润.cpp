#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices)
    {
        int n = prices.size();

        if (n == 0) {
            return 0;
        }

        vector<vector<int>> dp(n, vector<int>(2));

        for (int i = 0; i < n; i++) {
            if (i == 0) {
                dp[0][1] = -prices[0];
                dp[0][0] = 0;
            } else {
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
                dp[i][1] = max(dp[i - 1][1], -prices[i]);
            }
        }

        return dp[n - 1][0];
    }
};
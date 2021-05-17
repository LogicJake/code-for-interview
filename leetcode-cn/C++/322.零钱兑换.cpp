/*
 * @lc app=leetcode.cn id=322 lang=cpp
 *
 * [322] 零钱兑换
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount)
    {
        int n = coins.size();
        vector<vector<int>> dp(n, vector<int>(amount + 1, amount + 1));

        for (int i = 0; i < n; i++) {
            dp[i][0] = 0;
        }
        for (int j = 1; j <= amount; j++) {
            if (j >= coins[0]) {
                dp[0][j] = min(dp[0][j], dp[0][j - coins[0]] + 1);
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= amount; j++) {
                if (j >= coins[i]) {
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i]] + 1);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        if (dp[n - 1][amount] != amount + 1) {
            return dp[n - 1][amount];
        } else {
            return -1;
        }
    }
};
// @lc code=end

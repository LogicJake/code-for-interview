/*
 * @lc app=leetcode.cn id=1049 lang=cpp
 *
 * [1049] 最后一块石头的重量 II
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int lastStoneWeightII(vector<int>& stones)
    {
        int sum = 0;
        for (int stone : stones) {
            sum += stone;
        }

        int cap = sum / 2;
        int m = stones.size();
        vector<vector<int>> dp(m + 1, vector<int>(cap + 1, 0));

        for (int i = 1; i <= m; i++) {
            for (int j = 0; j <= cap; j++) {
                if (stones[i - 1] > j) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1]);
                }
            }
        }
        return sum - dp[m][cap] * 2;
    }
};
// @lc code=end

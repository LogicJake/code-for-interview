/*
 * @lc app=leetcode.cn id=494 lang=cpp
 *
 * [494] 目标和
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target)
    {
        int sum_ = 0;

        for (int num : nums) {
            sum_ += num;
        }

        int diff = sum_ - target;
        if (diff < 0 || diff % 2 == 1) {
            return 0;
        }

        int m = nums.size();
        int n = diff / 2;
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));
        dp[0][0] = 1;
        for (int i = 1; i <= m; i++) {
            int num = nums[i - 1];
            for (int j = 0; j <= n; j++) {
                dp[i][j] = dp[i - 1][j];

                if (num <= j) {
                    dp[i][j] += dp[i - 1][j - num];
                }
            }
        }

        return dp[m][n];
    }
};
// @lc code=end

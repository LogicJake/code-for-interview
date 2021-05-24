/*
 * @lc app=leetcode.cn id=664 lang=cpp
 *
 * [664] 奇怪的打印机
 */

// @lc code=start
class Solution {
public:
    int strangePrinter(string s)
    {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, INT_MAX));
        for (int i = n - 1; i >= 0; --i) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; ++j) {
                if (s[i] == s[j])
                    dp[i][j] = dp[i][j - 1];
                else //枚举区间内所有的可能性，取最优
                    for (int k = i; k < j; ++k)
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j]);
            }
        }
        return dp[0][n - 1];
    }
};
// @lc code=end

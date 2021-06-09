/*
 * @lc app=leetcode.cn id=879 lang=cpp
 *
 * [879] 盈利计划
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profit)
    {
        int MOD = (int)1e9 + 7;
        int m = group.size();
        vector<vector<vector<int>>> dp(m + 1, vector<vector<int>>(n + 1, vector<int>(minProfit + 1)));

        dp[0][0][0] = 1;

        for (int i = 1; i <= m; i++) {
            int members = group[i - 1], earn = profit[i - 1];
            for (int j = 0; j <= n; j++) {
                for (int k = 0; k <= minProfit; k++) {
                    if (j < members) {
                        dp[i][j][k] = dp[i - 1][j][k];
                    } else {
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - earn)]) % MOD;
                    }
                }
            }
        }

        int sum = 0;
        for (int j = 0; j <= n; j++) {
            sum = (sum + dp[m][j][minProfit]) % MOD;
        }
        return sum;
    }
};
// @lc code=end

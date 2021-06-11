/*
 * @lc app=leetcode.cn id=279 lang=cpp
 *
 * [279] 完全平方数
 */

// @lc code=start
#include <limits.h>
#include <vector>
using namespace std;
class Solution {
public:
    int numSquares(int n)
    {
        vector<int> dp(n + 1);

        for (int i = 1; i <= n; i++) {
            int num = INT_MAX;
            for (int j = 1; j * j <= i; j++) {
                num = min(num, dp[i - j * j]);
            }
            dp[i] = num + 1;
        }

        return dp[n];
    }
};
// @lc code=end

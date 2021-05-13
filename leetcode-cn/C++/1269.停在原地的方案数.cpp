/*
 * @lc app=leetcode.cn id=1269 lang=cpp
 *
 * [1269] 停在原地的方案数
 */

// @lc code=start
#include <algorithm>
#include <math.h>
#include <vector>
using namespace std;

class Solution {
public:
    const int MODULO = pow(10, 9) + 7;

    int numWays(int steps, int arrLen)
    {
        // dp[m][n] m=steps, n=min(steps, arrLen-1)
        int n = min(steps, arrLen - 1);
        vector<int> dp(n + 1, 0);
        dp[0] = 1;

        for (int i = 1; i <= steps; i++) {
            vector<int> dpNext(n + 1, 0);
            for (int j = 0; j <= n; j++) {
                dpNext[j] = dp[j];
                if (j >= 1) {
                    dpNext[j] = (dpNext[j] + dp[j - 1]) % MODULO;
                }
                if (j < n) {
                    dpNext[j] = (dpNext[j] + dp[j + 1]) % MODULO;
                }
                dp = dpNext;
            }
        }
        return dp[0];
    }
};
// @lc code=end
